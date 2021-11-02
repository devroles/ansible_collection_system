#!/usr/bin/env python
#
# Author: Greg Hellings - <ghelling@redhat.com> or <greg.hellings@gmail.com>
#
# Module to configure users in Jenkins authorized to use CLI
import xml.etree.ElementTree as ET
import os
from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = """
---
version_added: "2.1"
module: jenkins_cli_user
short_description: configure Jenkins CLI users with pub key
description:
  - This module configures admin users in Jenkins to utilize the specified
    SSH pubkey. Requires that role-based authentication be enabled and that
    a user be configured as an admin

options:
  jenkins_home:
    description:
     The root directory for the Jenkins install
    required: true
  jenkins_user:
    description:
      The name of the user to configure the SSH key for
  key_file:
    description:
      Path to the SSH keyfile to be listed as authorized
    required: true
  state:
    description:
      Currently limited to "present" - will create the user
    required: false

author: Gregory Hellings
"""


class UserList(object):
    def __init__(self, user_path):
        config = os.path.join(user_path, "users.xml")
        self.root = ET.parse(config).getroot()

    @property
    def users(self):
        if not hasattr(self, "_users"):
            mapping = self.root.find("idToDirectoryNameMap")
            if not mapping:
                return {}
            entries = mapping.getiterator("entry")
            if not entries:
                return {}
            users = {}
            for entry in entries:
                users[entry[0].text] = entry[1].text
            self._users = users
        return self._users


class User(object):
    def __init__(self, user_path, dirname):
        self.config = os.path.join(user_path, dirname, "config.xml")
        self.document = ET.parse(self.config)
        self.root = self.document.getroot()

    @property
    def keys(self):
        properties = self.root.find("properties")
        keys = properties.getiterator("authorizedKeys")
        return keys

    def add_key(self, pub_key):
        # If keys exist
        if self.keys:
            for key in self.keys:
                if pub_key not in str(key.text):
                    # No actual keys there, so create it, otherwise prepend
                    if key.text is None:
                        key.text = pub_key
                    else:
                        key.text = str(key.text) + "\n" + pub_key
                    return True
        # No keys exist
        else:
            properties = self.root.find("properties")
            xml = "org.jenkinsci.main.modules.cli.auth.ssh.UserPropertyImpl"
            ssh_auth = ET.SubElement(properties, xml)
            auth_key = ET.SubElement(ssh_auth, "authorizedKeys")
            auth_key.text = pub_key
            return True
        return False

    def save(self):
        self.document.write(self.config, encoding="UTF-8")


def main():
    module = AnsibleModule(
        argument_spec={
            "jenkins_home": {"required": True},
            "jenkins_user": {"required": True},
            "key": {"required": True},
            "state": {"choices": ["present"], "default": "present"},
        },
        supports_check_mode=False,
    )
    params = type("Params", (object,), module.params)
    user_path = os.path.join(params.jenkins_home, "users")
    changed = False

    # Check if user exists and find directory mapping
    users = UserList(user_path)
    if params.jenkins_user not in users.users.keys():
        module.fail_json(msg="No such user found." + users.users.keys())

    # Check user for configured key and add it
    user = User(user_path, users.users[params.jenkins_user])
    changed = user.add_key(params.key)
    if changed:
        user.save()
    module.exit_json(changed=changed)


main()
