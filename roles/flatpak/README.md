flatpak
===========

Makes sure that the flatpak app is installed on the target host

Requirements
------------

Ansible 2.8 or higher

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
- hosts: flatpak-servers
  roles:
    - role: devroles.system.flatpak
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
