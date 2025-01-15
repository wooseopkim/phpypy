from typing import Any

def eval(expression: str) -> Any:
    ...

def globals(name: str) -> Any:
    ...

def constant(name: str) -> Any:
    ...

def include(key: str) -> None:
    ...

def call(function: str, args: Any) -> Any:
    ...

__all__ = ["eval"]
