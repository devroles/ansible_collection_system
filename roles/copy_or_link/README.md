[![Build Status](https://travis-ci.org/devroles/copy_or_link.svg?branch=master)](https://travis-ci.org/devroles/copy_or_link)

COPY OR LINK
===========

When the connection mode is local, this role will create a symlink to the file
at its destination. When the connection mode is other than local, the files will
be uploaded to the destination.

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `copy_or_link_files` - List of files to process. Each element needs to minimally
  have a `src` and `dest` value. Moreover, each may have an optional `force`
  that will be passed to the `file` module when `state: link` is in place. See
  the documentation for the `force` paramemter on the `file` module in the
  Ansible documentation. The value of `force` will default to `false` when it is
  not present.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: copy_or_link-servers
  roles:
    - role: greg-hellings.copy_or_link
      copy_or_link_files:
        - src: /some/file
          dest: /remote/path/to/file
        - src: /some/directory
          dest: /remote/dir/path
          force: true
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
