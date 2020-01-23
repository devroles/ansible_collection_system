def test_service_running(host):
    server = host.service('mariadb')
    assert server.is_running
    assert server.is_enabled
