import configparser


def test_value_set(host):
    yum_conf_content = host.file('/etc/yum.conf').content_string
    yum_conf = configparser.ConfigParser()
    yum_conf.read_string(yum_conf_content)
    assert 'main' in yum_conf
    assert 'deltarpm' in yum_conf['main']
    assert not yum_conf['main'].getboolean('deltarpm')
