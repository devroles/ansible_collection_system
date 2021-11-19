adblock
===========

Creates and runs a container to install DNS-level adblocking software

Requirements
------------

You must be able to sudo/become the user that will own the files on the
system. And you need to become a user who can create that user and its
groups. So make sure you have pretty high sudo access or are root.

Ansible 2.9 or higher

Currently it's written targeting Fedora, but ultimately it just runs podman
containers, so any operating system that has podman installed *should* work.

Role Variables
--------------

Currently the following variables are supported:

### General

* `adblock_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `adblock_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: adblock-servers
  roles:
    - role: devroles.system.adblock
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
