import pytest


@pytest.mark.parametrize('name', [
    ('vim-X11'),
    ('google-chrome-stable'),
    ('virt-manager'),
    ('HandBrake-gui'),
    ('sound-juicer'),
    ('vlc'),
    ('entropypianotuner')
])
def test_package_installed(host, name):
    assert host.package(name).is_installed
