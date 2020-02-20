jenkins\_master
===============

Configure a Jenkins master service on the target system.

Dependencies
------------

You should create and configure a shell user who will be given access
to the Jenkins system. Typically this user is named "jenkins". You can use
the [users\_and\_groups](https://github.com/oasis-roles/users_and_groups)
role to handle this.

It's going to be necessary for you to setup the firewall before going on.
The [firewalld](https://github.com/oasis-roles/firewalld) role
can accomplish this. Minimally you'll want to open up the SSH port if
you want people from outside the host to be able to run Jenkins CLI commands,
and HTTP and/or HTTPS ports which you might want to proxy through something
else. One can be configured through the webserver role in this collection.

Before running this role, you should run the "jenkins" role in this collection,
which will do things like install Java, and setup the defined user for
running the service as.

Unless your distro provides a "jenkins" package, you will need to configure
a system repository. For instance, using the
[system\_repositories](http://github.com/oasis-roles/system_repositories) role.

Examples
--------

```yaml
- hosts: jenkins_master
  collections:
    - devroles.system
  roles:
    - roles: oasis_roles.firewalld
      firewalld_zone: public
      firewalld_ports_open:
        - proto: tcp
          port: 8888  # For Jenkins inspections
        - proto: tcp
          port: 50000  # Optional - for jswarm connections
      firewalld_services:
        - ssh  # Needed for external Jenkins CLI connections
        - http  # Needed if proxying through an HTTP server
        - https  # Needed if proxying through an HTTPS server
    - roles: oasis_roles.users_and_groups
      users_and_groups_add_modify_users:
        - jenkins
    - roles: oasis_roles.system_repositories
      system_repositories_repo_files: https://pkg.jenkins.io/redhat-stable/jenkins.repo
      system_repositories_rpm_keys: https://pkg.jenkins.io/redhat-stable/jenkins.io.key
    - roles: webserver
    - roles: jenkins  # pre-configures with things like Java
    - roles: jenkins_master
```
