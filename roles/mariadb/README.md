[![Build Status](https://travis-ci.org/devroles/mariadb.svg?branch=master)](https://travis-ci.org/devroles/mariadb)

MariaDB
===========

Installs and configures MariaDB on the target host system

Requirements
------------

Ansible 2.4 or higher

Linux

If you are running in Fedora, this role will only work properly if you are using
the system Python 3 interpreter. You can do this by setting the value of
`ansible_python_interpreter` to `/usr/bin/python3` in your host/group vars for
a system. You can, if you want to be cheeky, probably get away with setting it to
this only for the duration of this role but why do that?

Role Variables
--------------

Currently the following variables are supported:

### General

* `mariadb_databases` - A list of the names of databases to create on the
  target host
* `mariadb_user_privs` - A list of users and privileges to grant them on
  any target databases. Items in this list should be dictionaries in the form
  ```yaml
  - username: someuser
    database: rando_db
    privs: INSERT,DELETE # defaults to 'ALL'
    password: 'mypass' # Defaults to omit
  ```
  If omitted, the user will be granded 'ALL' permissions on the database.
  If the password for the user is omitted and the user does not exist, a user
  with no password will be created.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: mariadb-servers
  roles:
    - role: greg_hellings.mariadb
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
