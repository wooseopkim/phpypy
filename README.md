# phpypy

`phpypy` is a thin wrapper over [phpy](https://github.com/swoole/phpy). Begone all the hassles of building the library yourself, and just install this package.

### Development

- Don't forget to check out submodules too. I believe the command is [`git submodule update --init --recursive`](https://stackoverflow.com/a/1032653).
- [Install Pipenv](https://pipenv.pypa.io/en/latest/installation.html) and then `pipenv sync`. Then `pipenv shell` if you need it.
- Look into the `scripts` section defined in `Pipfile` to see what you could do. And the [workflow](./.github/workflows) files would be useful too.
- [nektos/act](https://github.com/nektos/act) command would be something like `act --artifact-server-path /tmp/artifacts --cache-server-path /tmp/cache`
