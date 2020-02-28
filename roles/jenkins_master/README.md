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

Variables
---------

The role currently accepts the following variables:
* `jenkins_home` - Default: `/var/lib/jenkins`. The root of where the service
will live. On RHEL/CentOS/Fedora systems this is `/var/lib/jenkins` if you
install the package from the jenkins.io repositories.
* `jenkins_user` - Default: `jenkins`. The user the Jenkins service will be
configured to run as.
* `jenkins_master_version` - Default: `2.204.2`. The version, from the RPM
construction, to install. The default is a (relatively current) LTS version.
* `jenkins_master_session_timeout` - Default: `480`. The number of minutes after
which to timeout a login session.
* `jenkins_master_heap_size` - Default: `3g`. Variable to pass to the JVM for
setting the maximum heap size. The default in most JVMs is very low. Combined
with `-Xmx` on the JVM command line.
* `jenkins_master_http_listen_address` - Default `<empty string>`. The host
address to bind the Jenkins HTTP process to. By default, this listens in
promiscuous mode. Ideally, you would set the service to listen only on loopback,
then bind the process behind a proxy like nginx.
* `jenkins_master_https_list_address` - Default `<empty string>`. The host
address to bind the Jenkins HTTPS process to. However, currently this role
does not permit the configuring of direct Jenkins serving HTTPS. Instead,
run SSL termination at a web proxy of some sort, then forward to the HTTP
port.

#### Advanced Options

These options are more advanced and are less likely for you to want to change.
However, they are presented as options to the user, in case they need to be
changed.

* `jenkins_master_debug_level` - Default `5`. The debugging level of output
for Jenkins to remember.
* `jenkins_master_enable_access_log` - Default `"no"`. If enabled, Jenkins will
log every HTTP call.
* `jenkins_master_handler_max` - Default: `100`. The number of threads Jenkins
should run to serve HTTP.
* `jenkins_master_handler_idle` - Default: `20`. The maximum number of Jenkins
HTTP service threads to have idle.
* `jenkins_master_args` - Default: `<empty string>`. A string of extra command
line options you want to pass to the Java JAR on bootup.
* `jenkins_master_java_extra_options` - Default `[]`. A list of extra options,
as string, to add to the JVM invocation. These extra options can be anything
that the JVM understand as an option. A number of defaults are already included,
but anything extra needed for your installation can be set here. Be sure to
shell escape anything that needs it.
* `jenkins_master_upgrade` - Default: `false`. Set to `true` if you are upgarding
between versions of Jenkins. Will cause the RPM to become unpinned so that yum
or dnf can do the upgrade. See note on next variable.
* `jenkins_master_block_upgrade` - Default: `false`. Set to true if you want
to prevent yum/dnf from accidentally upgrading the Jenkins package by masking
out the package in the package manager configuration. If you do this, then
want to upgrade the version, you need to either unmask the package yourself
or set `jenkins_master_upgrade` to `true` during the upgrade run. If you did
not set this to `true` during install, then you don't need to worry about the
`jenkins_master_upgrade` variable, either.
* `jenkins_master_ajp_port` - Default `8009`. The port to listen for AJP
connections on.
* `jenkins_master_ajp_listen_address` - Default `<empty string>`. The address
to bind to when listening for AJP connections. By default, we operate on all
host IPs.

#### VERY Advanced Options

These options are extra advanced and are even less likely for you to want to
mess with them unless you **really** know what you're doing.

* `jenkins_master_rpm` - Default: `jenkins-{{ jenkins_master_version }}-1.1`.
If you override this, then you'll be messing with the actual RPM install and
negating most value of the `jenkins_master_version` variable. Override it if
something is wonky and you have a different construction of the RPM or if you
have custom built RPMs in your repository that follow a different build
schema. You can also update this to a direct link to a Java RPM file if you
need to.
* `jenkins_master_java_cmd` - Default: `/usr/bin/java`. You can set this to
a custom value if you want, but you would be better to use your operating system
and its default mechanisms for selecting a JVM.
* `jenkins_master_soft_nofile_ulimit` - Default: `4096`. The name says it all
* `jenkins_master_hard_nofile_ulimit` - Default: `4096`. The name says it all
* `jenkins_master_soft_nproc_ulimit` - Default: `4096`. The name says it all
* `jenkins_master_hard_nproc_ulimit` - Default: `30654`. The name says it all!
* `jenkins_master_fsize_ulimit` - Default: `{{ ansible_memtotal_mb * 1024 }}`.
Sets an upper limit on the size of an open file, which should help prevent a
runaway job or malicious code from crippling the system too hard. This sets the
upper limit to the maximum size of the system's virtual memory, which should
more than handle a greedy process or core/heap dump.

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
