# phpypy

`phpypy` is a thin wrapper over [`phpy`](https://github.com/swoole/phpy). Begone all the hassles of building the library yourself, and just install this package.

### Development

1. Git Submodules

Don't forget to check out submodules too. I believe the command is [`git submodule update --init --recursive`](https://stackoverflow.com/a/1032653).

2. Local workflows

For [`nektos/act`](https://github.com/nektos/act), this would be a good starting point:

```bash
act --secret "$(gh auth token)" --artifact-server-path /tmp/artifacts --cache-server-path /tmp/cache --matrix platform:linux/amd64
```

You may want to keep those argument values in [`.actrc`](https://nektosact.com/usage/index.html?highlight=actrc#configuration-file).
