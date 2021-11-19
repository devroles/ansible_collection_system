[![Build Status](https://travis-ci.org/devroles/mariadb.svg?branch=master)](https://travis-ci.org/devroles/mariadb)

MariaDB
===========

Installs and configures MariaDB on the target host system

Requirements
------------

Ansible 2.4 or higher

Linux

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
