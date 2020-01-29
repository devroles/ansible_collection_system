def test_installed_package(host):
    assert host.package('vagrant-openstack-provider').is_installed
