import pytest


@pytest.mark.parametrize('name', [
    ('vim-enhanced'),
    ('git'),
    ('python3-libselinux'),
    ('mlocate'),
    ('openssh-server'),
    ('patch')
])
def test_package_installed(host, name):
    assert host.package(name).is_installed
