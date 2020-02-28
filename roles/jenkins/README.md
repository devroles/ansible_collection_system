Jenkins Common
--------------

A role to pre-configure the system for Jenkins use, both the driver system
and any jswarm worker systems that connect

Dependencies
------------

A system with an approrpriate service user pre-configured if necessary.

Variables
---------

The role currently supports the following variables:

* `jenkins_java_version` - Default: `11`. The version of Java to install on the
box. No checks are done in this role to ensure that the version is compatible
with either the remote host or to try and get it compatible with a particular
version of Jenkins. That responsibility is the user's.
* `jenkins_home` - Default: `/var/lib/jenkins`. The root where the Jenkins
home directory will live and where the system will be configured.
* `jenkins_user` - Default: `jenkins`. The system user that owns the files
under `jenkins_home` and who the server process will likely run as.
* `jenkins_user_home` - Default: `{{ jenkins_home }}`. The home directory of
the user indicated in `jenkins_user`. Usually this is the same as where the
`jenkins_home` is configured, as this is typically a system user and not a
typical login user.
