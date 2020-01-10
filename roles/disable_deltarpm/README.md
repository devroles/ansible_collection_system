[![Build Status](https://travis-ci.org/devroles/disable_deltarpm.svg?branch=master)](https://travis-ci.org/devroles/disable_deltarpm)

ROLE NAME
===========

Disables the deltarpm option on yum/dnf controlled systems

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

There are no settings for this

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: disable_deltarpm-servers
  roles:
    - role: greg_hellings.disable_deltarpm
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
