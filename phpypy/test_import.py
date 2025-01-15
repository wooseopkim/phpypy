def test_globals():
    from . import phpy

    env = phpy.globals("_ENV")

    assert env is not None
