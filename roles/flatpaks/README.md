flatpaks
===========

Basic description for flatpaks

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `flatpaks_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `flatpaks_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: flatpaks-servers
  roles:
    - role: oasis_roles.system.flatpaks
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>