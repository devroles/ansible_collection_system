def test_package_installed(host):
    assert host.package('qt5-qtwebengine-devel').is_installed
