[![Build Status](https://travis-ci.org/devroles/static_ip.svg?branch=master)](https://travis-ci.org/devroles/static_ip)

static\_ip
===========

Configures a NetworkManager-controlled connection with a given IP address.
The role only works on hosts where NetworkManager and DBus are both up and
running beforehand, and only manages connections that are under NetworkManager
control.

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `static_ip_addresses`. Default `{}`. A dict of objects. Each key is the
  NetworkManager connection name for the element. Required fiels are `address`,
  which is the CIDR-defined IPv4 address to add to the host and `gateway` which
  is the address of the default gateway for this connection. Optional fields
  are `dns`, which is an array of hosts to serve as the default DNS entries
  for this connection, max of 3. If this value is omitted, it will default to
  the value of `static_ip_dns`, documented below.
* `static_ip_dns`. Default ['8.8.8.8', '8.8.4.4']. A list of the default DNS
  entries to provide to an IP that doesn't have its own defed explicitly. The
  built-in defaults are the Google Public DNS entries and are decently safe,
  but most networks will have a local one that they prefer to use.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: static_ip-servers
  roles:
    - role: oasis_roles.static_ip
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
