# Styling

## GTK CSS

sora uses [GTK CSS](https://docs.gtk.org/gtk3/css-overview.html) for styling. You can style your widgets using either [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) or [Sass](https://sass-lang.com/).
GTK CSS is similar to Vanilla CSS, but does not support all CSS Properties.
Checkout the [Supported CSS Properties](https://docs.gtk.org/gtk3/css-properties.html) for more information.

The styles are loaded from the config directory and sora looks for a `style.scss` or `style.css` file.

## GTK Debugger

You can use the GTK Debugger to inspect the widgets and their properties.

To start sora with the GTK Debugger, use the `--inspector` flag.

```bash
$ sora start --inspector
```
