epel
===========

Installs EPEL packages in variants of Enterprise Linux such as CentOS, RHEL,
OracleLinux, etc. If the role is missing a distro you really want, let me know

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `epel_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `epel_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: epel-servers
  roles:
    - role: devroles.system.epel
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
