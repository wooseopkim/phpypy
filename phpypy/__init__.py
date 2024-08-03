"""
A Python-side wrapper for swoole/phpy
"""

__version__ = "0.0.1"

import sys
import os
import platform

os_name = {
    "Linux": "linux",
}[platform.system()]
os_arch = {
    "x86_64": "amd64",
}[platform.machine()]
lib_path = os.path.join(os.path.dirname(__file__), "..", "lib", os_name, os_arch)

if not os.getenv("LD_LIBRARY_PATH", None):
    os.environ["LD_LIBRARY_PATH"] = f"{lib_path}:{os.getenv('LD_LIBRARY_PATH', '')}"
    os.execv(sys.executable, [sys.executable, sys.argv[0]])


sys.path.append(lib_path)


import phpy  # noqa: E402

__all__ = ["phpy"]
