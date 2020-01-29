[![Build Status](https://travis-ci.org/devroles/virtualenv_ansible_python.svg?branch=master)](https://travis-ci.org/devroles/virtualenv_ansible_python)

virtualenv_ansible_python
===========

Ever have an instance where you're trying to run a playbook and you need a particular Python package
to support that one Ansible module, but you just can't find a system package for it anywhere? Or it lives
in someone's package module repo that has way too much cruft, or you don't know whether it will continue
existing and stay updated long enough? Or you don't trust the responsible parties?

This role will stand up a virtualenv in a temporary directory, install a list of pip packages into it, and
then set that virtualenv as the Python interpreter for the rest of the playbook. Never fear, though. It will
register the existing interpreter to the variable `virtualenv_ansible_python_original_interpreter` so that
you can always go back to it in the future, if you need to.

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `virtualenv_ansible_python_packages` - default: empty list. A list of packages
  to install to the virtualenv. These need to be a list of dicts in the form
  `{"name": "some_pkg", "version": "123"}` where the "version" key is optional
  and will default to the latest stable version on PyPI when.
* `virtualenv_ansible_python_site_packages` - default: true. Flag determining if the Virtualenv should
  be created with all the system packages already present. Usually this is a good thing, and is very
  important on RHEL/CentOS/Fedora systems when SELinux is eanbled, as the Python libselinux bindings
  are not easily installed into a virtualenv otherwise.
* `virtualenv_ansible_python_dir` - Leave this blank if you want this role to create a new tempdir
  version of Python to hold the virtualenv. If you want to use an existing virtualenv or a pre-determined
  path to the executable, then you can specify this as the root of the virtualenv to be created
* `virtualenv_ansible_python_original_interpreter` - this is not an input variable but will contain
  the path to the original Python interpreter that was executing modules coming into this role. So this
  is more of an output/return type of variable

Dependencies
------------

A sysmte with virtualenv available

Example Playbook
----------------

```yaml
- hosts: virtualenv_ansible_python-servers
  roles:
    - role: greg_hellings.virtualenv_ansible_python
      virtualenv_ansible_python_packages:
        - dnspython
        - openstacksdk
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
