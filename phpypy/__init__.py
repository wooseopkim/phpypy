"""
A Python-side wrapper for swoole/phpy
"""

__version__ = "0.0.1"

from phpypy import _import_guard as _import_guard  # noqa: I001
import phpy


def cli():
    import sys
    for arg in sys.argv[1:]:
        phpy.eval(arg)

__all__ = ["phpy"]
