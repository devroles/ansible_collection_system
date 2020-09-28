molecule_vagrant_ci
===========

Basic description for molecule_vagrant_ci

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `molecule_vagrant_ci_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `molecule_vagrant_ci_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: molecule_vagrant_ci-servers
  roles:
    - role: oasis_roles.system.molecule_vagrant_ci
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>