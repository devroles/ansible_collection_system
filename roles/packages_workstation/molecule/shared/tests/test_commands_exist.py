import pytest


@pytest.mark.parametrize('cmd', [
    ('g++'),
    ('jq'),
    ('python3'),
    ('tox'),
    ('ansible-lint'),
    ('make'),
    ('ffmpeg'),
    ('packerio'),
    ('vagrant')
])
def test_command(host, cmd):
    assert host.exists(cmd)
