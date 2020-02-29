jenkins\_configure
==================

Configures a Jenkins master that is already installed on the target host.

Dependencies
------------

You should already have a Jenkins master installed and running on the host
before running this role. That can be done with the `jenkins_master` role
in this collection. Although that role is specific to CentOS/Fedora/RHEL,
this role doesn't try to be (that one doesn't *try* to be, either, but it
just is for the time being).

Variables
---------

#### Jenkins installation variables

* `jenkins_home` - Default: `/var/lib/jenkins`. The directory path where the
root of the Jenkins installation lives.
* `jenkins_user` - Default: `jenkins`. The owner of the files in `jenkins_home`
and the system user who the `jenkins` process executes as.
* `jenkins_configure_plugins` - Please consult the code for the default list
here, it's pretty extensive. A few of them are necessary for this role to
run through to completion, such as auth or such if you have that configured.
This is a dict, not a list, of plugins. The name of each key is the name of
the plugin, and each plugin can have an optional field for "version" at which
to install and "pinned" which is a boolean flag to say if you want that
plugin to be pinned. e.g.
```yaml
jenkins_configure_plugins:
  ansible:
    version: 1.0
    pinned: true
  blueocean:  # will install the latest at the first-run of this role
  blueocean-config:
    pinned: false  # Will un-pin the plugin if it was previous pinned
```

#### Auth/access variables

* `jenkins_configure_security_enabled` - Default: `false`. Will disable all
login requirements. **YOU PROBABLY DON'T WANT THIS, AND SHOULD SET IT TO TRUE.**
* `jenkins_configure_admin` - Default: `{"name": "admin", "email": "root@localhost",
"password": "changeme"}`. A default, base, admin user to create on the system
and to assign to the "admin" role. You will likely want to change this.
* `jenkins_configure_admin_sids` - Default: `[]`. A list of user system ids (names)
to grant admin privileges to.
* `jenkins_configure_cli_users` - Default: `[]`.
* `jenkins_configure_local_users` - Default: `[]`. A list of local users to
create regardless of auth mechanisms. Each element in the array should have
the same structure as the `jenkins_configure_admin` dict.
* `jenkins_configure_security_extra_roles` - Default: `[]`. An array of roles
and their permissions to add to Jenkins. A role called "admin" will always be
created that has EVERY permission. You can override this by adding an item
to this list with that name. Each element should be of the structure (this is
the actual structure used to create the "anonymous" role that gives people the
ability to at least pull up the local page.
```yaml
name: anonymous
permissions:
  - com.synopsys.arc.jenkins.plugins.ownership.OwernshipPlugin.Jobs
  - hudson.model.Hudson.Read
  - hudson.model.View.Read
sids:
  - anonymous
```
* `jenkins_cli_shell_user` - Default: `ansible_user_id`. The system user who
will be configured with SSH access to the Jenkins shell. Typically this will
not be the same user who the Jenkins instance runs as, as this would allow
any and every job to have admin access to the Jenkins instance. And that would
be a bad idea.
* `jenkins_cli_shell_user_home` - Default: `ansible_user_dir`. The home
directory of the shell user, where their SSH key can be found.
* `jenkins_configure_ldap` - Default: undefined. This is a dict that, if
defined AND if `jenkins_configure_security_enabled` is set to true, will
configure the LDAP plugin on the system. This is untested, though it was working
back in the day. Structure looks like this (enjoy deciphering what each one means).
```yaml
jenkins_configure_ldap:
  server: ldaps://ldap.example.com
  root_dn: dc=example,dc=com
  user_search_base: ''
  user_search: uid={0}
  group_search_base: ou=groups
  group_search_filter: "(& (cn={0}) (objectclass=posixGroup))"
  group_membership: memberUid={1}
  display_name_attr: displayname
  email_addr_attr: mail
  manager_dn: ''
  manager_password: ''
```


#### Advanced Variables

* `jenkins_configure_envvars`. Default:
```yaml
- key: JENKINS_MASTER_URL
  value: "{{ jenkins_configure_url }}"
```
A list of dictionaries. Each item in the list will be exposed in the envvars
of every job run on this system with the specified value. The default is just
to set the `JENKINS_MASTER_URL`, which is needed for some of the plugins and
can be useful elsewhere.
* `jenkins_slave_agent_port` - Default: `50000`. Port that slave/worker agents
will use to connect to the system.
* `jenkins_configure_update_centers` - Default:
```yaml
- id: default
  url: "https://mirror.xmission.com/jenkins/updates/update-center.json"
```
A list of update centers to configure on the system.
