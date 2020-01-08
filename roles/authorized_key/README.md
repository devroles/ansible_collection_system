Authorized Keys
===========

Configures the current user's SSH key as an authorized key on the remote system

Requirements
------------

Ansible 2.4 or higher

A Linux host

An id\_rsa.pub file in the current user's .ssh directory

Role Variables
--------------

Currently the following variables are supported:

### General

There are currently no configurable variables

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: authorized_key-servers
  roles:
    - role: greg_hellings.authorized_key
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
