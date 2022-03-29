packages_server
===========

The packages tha I want installed on all of my server devices

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `packages_server_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `packages_server_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: packages_server-servers
  roles:
    - role: devroles.system.packages_server
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
