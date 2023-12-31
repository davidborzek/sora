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
    - [`gtk3`](https://archlinux.org/packages/extra/x86_64/gtk3/)
    - [`python-gobject`](https://archlinux.org/packages/extra/x86_64/python-gobject/)
    - [`python-libsass`](https://aur.archlinux.org/packages/python-libsass)<sup>AUR</sup>

=== ":simple-fedora: Fedora"

    - [`python3`](https://packages.fedoraproject.org/pkgs/python3.10/python3/)
    - [`meson`](https://packages.fedoraproject.org/pkgs/meson/meson/)
    - [`python3-gobject`](https://packages.fedoraproject.org/pkgs/pygobject3/python3-gobject/)
    - [`gtk3`](https://packages.fedoraproject.org/pkgs/gtk3/gtk3/)
    - [`python3-libsass`](https://packages.fedoraproject.org/pkgs/python-libsass/python3-libsass/)

```shell
$ git clone https://github.com/davidborzek/sora.git
$ cd sora
$ meson setup --prefix=/usr builddir
$ ninja -C builddir install
```
