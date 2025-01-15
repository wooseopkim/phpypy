def test_globals():
    from . import phpy

    env = phpy.globals("_ENV") # type: ignore

    assert env is not None
