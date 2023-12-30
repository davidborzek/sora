project('sora',
    meson_version: '>= 0.59.0'
)

python = import('python')

py_installation = python.find_installation('python3')

if not py_installation.found()
    error('No valid python3 binary found')
endif

if not py_installation.language_version().version_compare('>= 3.10')
  error('Python 3.10 or newer is required.')
endif

install_subdir(
    'sora',
    install_dir: py_installation.get_install_dir()
)

install_data(
    'bin/sora',
    install_dir : get_option('bindir'),
)
