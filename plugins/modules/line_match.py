#!/usr/bin/env python

import re
from ansible.module_utils.basic import AnsibleModule
from os import path


def main():
    module = AnsibleModule(
        argument_spec={
            'file': {'required': True},
            'line': {'required': False},
            'method': {'choices': ['regex', 'simple'], 'default': 'simple'}
        }
    )
    # First sanity check that the file exists and is not a directory or such
    if not path.exists(module.params['file']) or \
       not path.isfile(module.params['file']):
        module.exit_json(changed=False, exists=False, present=False)
    # Create the method that will do the matching
    if module.params['method'] == 'regex':
        expression = re.compile(module.params['line'])

        def matcher(x):
            return expression.search(x) is not None
    else:
        def matcher(x):
            return x == module.params['line']
    # Read the file, line by line, and check for matches
    with open(module.params['file'], 'r') as reader:
        for line in reader.readlines():
            if matcher(line):
                module.exit_json(changed=False, exists=True, present=True)
    module.exit_json(changed=False, exists=True, present=False)


main()
