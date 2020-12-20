mta
===========

Sets up a mail transfer agent on a host

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `mta_domains` - a list of domain names to receive mail for and to
configure mail.{{ item }} webhost on

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
