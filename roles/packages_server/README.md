packages_server
===========

Basic description for packages_server

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
    - role: oasis_roles.system.packages_server
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>
