import pytest


@pytest.mark.parametrize('name', [
    ('vim-X11'),
    ('google-chrome-stable'),
    ('virt-manager'),
    ('HandBrake-gui'),
    ('vlc')
])
def test_package_installed(host, name):
    assert host.package(name).is_installed
