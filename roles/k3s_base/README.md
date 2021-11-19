k3s_base
===========

Basic description for k3s_base

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `k3s_base_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `k3s_base_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: k3s_base-servers
  roles:
    - role: oasis_roles.system.k3s_base
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>
