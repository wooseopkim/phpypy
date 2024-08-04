"""
A Python-side wrapper for swoole/phpy
"""

__version__ = "0.0.1"

from . import _import_guard as _import_guard
import phpy

__all__ = ["phpy"]
