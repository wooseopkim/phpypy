"""
A Python-side wrapper for swoole/phpy
"""

__version__ = "0.0.1"

import phpy
from phpypy import _import_guard as _import_guard


def cli():
    import sys
    for arg in sys.argv[1:]:
        phpy.eval(arg)

__all__ = ["phpy"]
