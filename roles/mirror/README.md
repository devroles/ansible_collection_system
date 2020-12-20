Mirror
===========

Sets up a mirror rsync script and configures SELinux options
to allow rsync clients to control the files there

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
    - role: devroles.system.mirror
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
