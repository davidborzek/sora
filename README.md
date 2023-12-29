# sora

sora is an experimental widget system, extendable and configurable using python and based on GTK3.
You can create your own widgets in any window manager.

It is heavily inspired by some existing widget systems and window managers, see [Credits](#credits).

> Note: sora is still in development, and not ready for production use.
> You should expect breaking changes for the configuration api.
> Currently only x11 is supported.

# Getting Started

Follow the [wiki](https://davidborzek.github.io/sora/) for more information.

# Development

## Requirements

- python3
- gtk3
- libsass

## Running locally

```bash
$ ./bin/sora start -c .config/
```

> Note: You should create a local config directory at `.config/` for development.
> Otherwise, sora will use the default config directory at `$XDG_CONFIG_HOME/sora`.

# Credits

- [eww](https://github.com/elkowar/eww)
- [ags](https://github.com/Aylur/ags)
- [awesomewm](https://github.com/awesomeWM/awesome)
- [qtile](https://github.com/qtile/qtile)
