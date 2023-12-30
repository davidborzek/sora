# Installation

## From source

**Prerequisites**

=== ":simple-ubuntu: Ubuntu / :simple-debian: Debian"

    - `python3`
    - `meson`
    - `python3-gi`
    - `gir1.2-gtk-3.0`
    - `python3-libsass`

=== ":simple-archlinux: Arch Linux"

    - [`python`](https://archlinux.org/packages/core/x86_64/python/)
    - [`meson`](https://archlinux.org/packages/extra/any/meson/)
    - [`python-gobject`](https://archlinux.org/packages/extra/x86_64/python-gobject/)
    - [`python-libsass`](https://aur.archlinux.org/packages/python-libsass)<sup>AUR</sup>

```shell
$ git clone https://github.com/davidborzek/sora.git
$ cd sora
$ meson setup --prefix=/usr builddir
$ ninja -C builddir install
```
