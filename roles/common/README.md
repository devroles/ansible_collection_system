[![Build Status](https://travis-ci.org/devroles/copy_or_link.svg?branch=master)](https://travis-ci.org/devroles/copy_or_link)

Dev setup
===========

Prepares a system to do basic development

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* None

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: copy_or_link-servers
  roles:
    - role: devroles.system.dev
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
