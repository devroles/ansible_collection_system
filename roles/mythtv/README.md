[![Build Status](https://travis-ci.org/devroles/mythtv.svg?branch=master)](https://travis-ci.org/devroles/mythtv)

MythTV
===========

This role installs the basic software needed to configure MythTV and install
the firmware bundle needed to pair with a Hauppage 950 USB capture card. This
is highly specific, but it's the card that I, as the writer of this role, have.
If you have a different card, feel free to fork this or to provide a PR to
update it to also include your firmware. There's no real problem with having
more of the firmware available than necessary.

Requirements
------------

Ansible 2.4 or higher

MySQL needs to be running on the target host. Currently this role doesn't
support running MySQL on a remote host, although I don't know that setting it
up would be terrible difficult. If you would like to help tackle that, please
feel free to submit a PR. Configuring MySQL can be done with the
[greg\_hellings.mysql](https://github.com/devroles/mysql) role.

Role Variables
--------------

Currently the following variables are supported:

### General

* `mythtv_db_username` - Username to connect to MySQL database. Optional if
  either ~/.my.cnf is configured on the host or password-free login as 'root'
  is configured.
* `mythtv_db_password` - Password to connect to MySQL database. Optional if
  either ~/.my.cnf is configured on the host or password-free login as 'root'
  is configured.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: mythtv-servers
  roles:
    - role: greg_hellings.mythtv
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
