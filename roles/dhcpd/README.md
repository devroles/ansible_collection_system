[![Build Status](https://travis-ci.org/devroles/dhcpd.svg?branch=master)](https://travis-ci.org/devroles/dhcpd)

dhcpd
===========

Installs and configures a basic DHCP server for handling local server
traffic. It does not (yet) handle complex cases, pools, shared networks
or the like. It handles simple sets of subnets and specific host
configuration values

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `dhcpd_authoritative` - Required. Set to true if this is the main or only
  DHCP server for its network. Set to false, otherwise.
* `dhcpd_subnets` - Technically optional, but without it, the server will not
  respond to any requests, as it will not have any addresses it wants to handle.
  Elements in this array need to minimally have the field values `address` and
  `netmask` to define the network that they are attached to. Likewise, they
  must have a `start` and `end` address that define the range of addresses that
  will be served for this subnet and the field `routers` which is an array of
  addresses for the edge routers of the network.

  The parameter `allow_all`, which defaults to true, can be set to `false` if
  only pre-configured hosts in the defined array are to be handled. If you want
  this server to operate in the "normal" way where it hands out leases to most
  systems connecting to the network, then leave this as a default.

  Additional optional fields are `parameters`, which is an array of parameters
  that can apply to a particular subnet, listed in the order to configure them.
  Also a similar array of strings named `declarations` will be added to the
  subnet definition as well.
* `dhcpd_hosts` - An optional array of specific host entries that deserve their
  own configuration section. Minimally each entry needs the fields `hostname`,
  `ethernet`, and `address`. `hostname` is a string to uniquely identify the
  host in the configuration file. `ethernet` is the Ethernet MAC address of the
  system that is being configured. `address`, although the mnemnoic is singular,
  accepts an array of addresses that could be assigned to the host depending on
  what subnet it connecting from.

  Additional optional fields include `booting`, which allows the system to be
  brought up properly and `duplicates`, which can help the system avoid
  address thrashing when the same physical machine might have multiple OS or
  other confiugration issues which could cause it to not appear identically to
  the server. Both of these are enabled by default and probably should be left
  as-is.
* `dhcpd_domain` - Default ignored. Set this if you want to tell clients the
  default domain they will be attached to.
* `dhcpd_lease_time` - The default length of a DHCP lease, in seconds. Defaults
  to 600.
* `dhcpd_max_lease_time` - The maximum length of time, in seconds, to offer a
  DHCP lease for. Defaults to 7200.
* `dhcpd_ddns_update_style` - Valid values are "none", "standard", and "interim".
  The value "interim" should not be used in new deployments. The value of "none"
  will effectively disable updating of the DNS with hostnames while the value
  "standard" will follow published standards. The dhcpd server normally allows
  this, but the default in this role is "none".
* `dhcpd_bootp` - Default true. Enables responoding to BOOTP requests.
* `dhcpd_declines` - Default false. Ignores when a client declines to accept
  an address. Repsonding to this would allow a malicious actor to stress the
  server by repeatedly denying to accept valid responses.
* `dhcpd_leasequery` - Default false. Allows clients to query the system to
  discover the status of a lease.
* `dhcpd_lease_file` - Default /var/lib/dhcpd/dhcpd.leases. Probably best to
  leave this alone. Changes the file where lease values are held.
* `dhcpd_port` - Default 67. Again, probably best to leave this alone. Changes
  the UDP port that the server listens on.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: dhcpd-servers
  roles:
    - role: oasis_roles.dhcpd
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>
