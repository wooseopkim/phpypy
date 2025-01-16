"""
A Python-side wrapper for swoole/phpy
"""

__version__ = "0.0.1"

import phpypy._import_guard as _  # noqa: F401, I001 # pyright: ignore[reportUnusedImport]
import phpy


def cli():
    import sys

    for arg in sys.argv[1:]:
        phpy.eval(arg)


__all__ = ["phpy"]
