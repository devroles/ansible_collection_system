import pytest


@pytest.mark.parametrize("path, owner, mode", [
    ("/mnt/defaults", "root", 0o755),
    ("/mnt/cloud-user", "cloud-user", 0o755),
    ("/mnt/restricted-access", "root", 0o700)
])
def test_is_mounted(host, path, owner, mode):
    with host.sudo():
        fs = host.mount_point(path)
        file_path = host.file(path)
        assert fs.exists
        assert fs.filesystem == 'ext4'
        assert file_path.user == owner
        assert file_path.is_directory
        assert file_path.mode == mode
