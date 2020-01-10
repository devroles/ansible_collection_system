import configparser


def test_value_set(host):
    dnf_conf_content = host.file('/etc/dnf/dnf.conf').content_string
    dnf_conf = configparser.ConfigParser()
    dnf_conf.read_string(dnf_conf_content)
    assert 'main' in dnf_conf
    assert 'deltarpm' in dnf_conf['main']
    assert not dnf_conf['main'].getboolean('deltarpm')
