import os
import platform
import sys


def os_name():
    match platform.system():
        case "Linux":
            return "linux"
        case _:
            return "unknown"


def os_arch():
    match platform.machine():
        case "x86_64":
            return "amd64"
        case "aarch64":
            return "arm64"
        case _:
            return "unknown"


working_directory = os.path.dirname(__file__)
raw_path = os.path.join(working_directory, "..", "lib", os_name(), os_arch())
lib_path = os.path.normpath(raw_path)

if not len([x for x in os.listdir(lib_path) if x.endswith(".so")]):
    raise Exception(f"libraries are not found under {lib_path}")

if not os.getenv("LD_LIBRARY_PATH", None):
    os.environ["LD_LIBRARY_PATH"] = f"{lib_path}:{os.getenv('LD_LIBRARY_PATH', '')}"
    os.execv(sys.executable, [sys.executable] + sys.argv)


sys.path.append(lib_path)
