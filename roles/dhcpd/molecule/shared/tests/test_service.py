def test_service(host):
    assert host.service('dnsmasq').is_running
