def test_table_file_exists(host):
    with host.sudo():
        assert host.file('/var/lib/mysql/testdb/abc.frm').exists


def test_original_test_database_deleted(host):
    with host.sudo():
        assert not host.file('/var/lib/mysql/test').exists
