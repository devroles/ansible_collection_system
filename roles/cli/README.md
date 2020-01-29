CLI
===========

Configures system repositories and installs CLI based tools that I have found
useful in my work. Also configures a number of basic systems for use on my
systems. Repos configured include most of the common RPMFusion repos that are
usually considered vital to happily dealing with multimedia in Linux.

In addition to a large number of basic command line packages that I use in
a wide variety of settings (build tools, the vim editor, git, etc), there are
also a number of services that are setup by this role that I find very useful.

Such things include configuring the system to handle Vagrant the way I like it,
configuring libvirt, kerberos, packer, and getting as much of the system
ready for Blu ray usage as I can manage. It will also install a group of
virtualenvs in the user directory that include a large number of tools that I
use in my daily life.

Requirements
------------

Ansible 2.4 or higher

A Linux system running Fedora (or possibly CentOS)

Role Variables
--------------

Currently the following variables are supported:

### General

* `cli_libvirt_storage` - filesystem path to use for libvirt's storage of
  images and VM systems. The system default is to put this somewhere under
  /var, but I default it to /home/libvirt in this role, as I usually have a
  much larger partition holding /home than I have in /var

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: cli-servers
  roles:
    - role: cli
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
