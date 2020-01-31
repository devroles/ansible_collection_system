devroles.system.webserver
=========================

Installs and configures a system webserver including optionally enabling HTTPS
with LetsEncrypt.

Both port 80 and port 443 are available, as is an optional redirect from
www.foo.com to foo.com. The files served for both will be the same ones out of
the /var/www/foo.com directory. Inasmuch as the system and Nginx suppor it, both
IPv4 and IPv6 are supported.

Hosts that have https enabled will have a certificate auto-generated with
LetsEncrypt, and therefore need to be visible on the public Internet. At a later
time I might update this role to include support for pre-generated certificates.

As an implementation detail, this role will install Nginx as well as PHP and
configure them together.

Dependencies
------------

Linux system, specifically CentOS/Fedora/RHEL. The role could be readily adopted
to other operating systems, but until a PR is submitted or I personally need to
run a server on a different system, things like the package name are limited to
only being tested in the Cent/Fedora orbit.

Variables
---------

The following options are available for this role:

* `webserver_domains` - A list of the domains and their options to configure.
  Each element in the domain looks like this:
  ```yaml
- tld: host.domain.com
  redirect: true  # optional, default true. Redirect www.<tld> to <tld>
  http: false  # optional, default true. Serve unencrypted over port 80
  https: true  # optional, default true. Serve encrypted over port 443
  index: true  # optional, default false. Enable directory auto-listing
```
  When the `https` option is enabled, this role will attempt to auto-generate
  an SSL certificate and have it automatically encrypted with LetsEncrypt, so
  that you don't need to worry about that.
* `webserver_acme_directory` - The endpiont for letsencrypt. This is set to a
  reasonable default value and shouldn't need to be changed unless you
  specifically want to hit a different ACME server.

Author
------
Greg Hellings <greg.hellings@gmail.com>
