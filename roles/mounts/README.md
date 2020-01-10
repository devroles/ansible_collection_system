[![Build Status](https://travis-ci.org/devroles/mounts.svg?branch=master)](https://travis-ci.org/devroles/mounts)

Mounts
===========

Creates mount points, adds them to fstab, and mounts them onto your system

Requirements
------------

Ansible 2.4 or higher

Linux

Role Variables
--------------

Currently the following variables are supported:

### General

* `mounts` - A list of mount points and their settings. Each element should take
  the following form:
  ```yaml
  - mount_point: /path/to/mount/location
    device: /dev/qxda1
    fstype: ext4
    owner: cloud-user # optional - user to own mount point directory
    group: wheel # optional - group to own mount point directory
    mode: 0755 # optional - fs mode to set on mount point directory
    dump: 0 # optional - see fstab manpage
    passno: 0 # optional - see fstab manpage
    opts: noauto # optional - options passed to mount
  ```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: mounts-servers
  roles:
    - role: greg_hellings.mounts
  vars:
    mounts:
      - mount_point: /mnt/data
        fstype: xfs
        device: /dev/sdb1
        opts: noauto,ro
      - mount_point: /mnt/shared
        fstype: ext4
        device: /dev/disk/by-label/shared
        dump: 1
        owner: httpd
        group: httpd
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
