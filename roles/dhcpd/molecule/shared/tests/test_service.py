def test_service(host):
    assert host.service('dhcpd').is_running
