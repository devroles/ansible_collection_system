[![Build Status](https://travis-ci.org/oasis-roles/dns_server.svg?branch=master)](https://travis-ci.org/oasis-roles/dns_server)

dns_server
===========

Basic description for dns_server

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `dns_server_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: dns_server-servers
  roles:
    - role: oasis-roles.dns_server
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>