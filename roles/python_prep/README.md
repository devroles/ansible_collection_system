[![Build Status](https://travis-ci.org/devroles/python_prep.svg?branch=master)](https://travis-ci.org/devroles/python_prep)

Python Prep
===========

Sometimes there is a need for additional packages to be installed right at the
very beginning of a playbook. For instance, on Fedora the version of Python that
is shipped does not have the python{2,3}-dnf package installed that the dnf
module in Ansible leverages in order to do its work. This role will fulfill the
efforts that you need to get Python up and running for later in your playbook

Requirements
------------

Ansible 2.0 or higher

A version of Linux

Role Variables
--------------

Currently the following variables are supported:

### General

* `python_prep_become` - Defaults to `true`. Whether to use the `become` method
  in Ansible to execute installs as a different user than default.
* `python_prep_become_user` - Defaults to `root`. The user to escalate privs to
  when doing the install.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: python_prep-servers
  roles:
    - role: greg_hellings.python_prep
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
