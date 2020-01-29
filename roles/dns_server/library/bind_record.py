from ansible.module_utils.basic import AnsibleModule
from dnszone import dnszone
from os import path


dns_entry_types = ['A', 'AAAA', 'MX', 'TXT', 'CNAME', 'SOA']


class Domain(dnszone.Zone):
    def __init__(self, module, params):
        super(Domain, self).__init__(params.domain)
        self._module = module
        self._params = params
        if not path.exists:
            self._changed = True
        else:
            self.load_from_file(params.path)

    def contains_name(self, name=None):
        if name is None:
            name = self._params.name
        names = self.get_names()
        if self._params.name in names.keys():
            self._name = names[self._params.name]
            return True
        return False

    def add_name(self, name):
        if not self.contains_name(name):
            self._changed = True
        return super(Domain, self).add_name(name)

    def delete_name(self, name):
        if self.contains_name(name):
            self._changed = True
        super(Domain, self).delete_name(name)

    def is_changed(self):
        return self._changed


def main():
    module = AnsibleModule({
        'path': {'required': True, 'type': 'path'},
        'domain': {'required': True},
        'type': {'choices': dns_entry_types},
        'name': {'required': True},
        'value': {'type': 'str'},
        'priority': {'type': 'int'},
        'state': {'choices': ['present', 'absent'], 'default': 'present'},
        'mname': {'type': 'str'},
        'rname': {'type': 'str'},
        'refresh': {'type': 'int'},
        'retry': {'type': 'int'},
        'expire': {'type': 'int'},
        'ttl': {'type': 'ttl'}
    },
        required_if=[
            ('state', 'present', ['value', 'type']),
            ('type', 'SOA', ['mname', 'rname', 'refresh', 'retry', 'expire',
                             'ttl'])
        ]
    )
    params = type('Args', (object,), module.params)
    # Do more complicated variable combination verifications to avoid errors
    # down the line
    #
    # MX records require a string AND a priority code
    if params.state == 'present' and params.type == 'MX' and \
            'priority' not in params.keys():
        module.fail_json(msg="MX records require a priority to be set")
    # If you're removing from the root '@' node, you must choose a type
    if params.state == 'absent' and params.name == '@' and \
            'type' not in module.params:
        module.fail_json(msg="You must specify a type to delete from root")
    # Can't remove an SOA
    if params.state == 'absent' and params.type == 'SOA':
        module.fail_json(msg="This module does not support removing the SOA")
    changed = False
    zone = Domain(module, params)
    # Perform the work of the module
    if params.state == 'absent':
        # Delete a root entry, such as MX or NS
        if params.name == '@':
            names = zone.root.records(params.type).items
            if params.name in names:
                names.delete(params.name)
                changed = True
        # Delete an entire name, all types
        elif 'type' not in module.params:
            zone.delete_name(params.name)
        # Delete only the particular type
        else:
            zone.names
    else:
        if params.type == 'SOA':
            pass
