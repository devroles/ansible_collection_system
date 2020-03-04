def test_mirror_script_exists(host):
    assert host.file('/var/mirror/centos.sh').exists


def test_mirror_dir_exists(host):
    f = host.file('/var/mirror/8/cr')
    assert f.exists
    assert f.is_directory


def test_excludes_worked(host):
    assert not host.file('/var/mirror/8/BaseOS').exists
