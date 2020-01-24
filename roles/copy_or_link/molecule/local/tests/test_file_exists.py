import pytest


@pytest.mark.parametrize('name,content', [
    ('/root/first', 'First file\n'),
    ('/root/second', 'Second file\n')
])
def test_file(host, name, content):
    f = host.file(name)
    assert f.exists
    assert f.content_string == content
    assert f.is_symlink