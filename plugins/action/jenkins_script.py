from ansible.errors import AnsibleAction
from ansible.plugins.action import ActionBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display

    display = Display()


class ActionModule(ActionBase):
    def __init__(self, *args, **kargs):
        super(ActionModule, self).__init__(*args, **kargs)

    def run(self, tmp=None, task_vars=None):
        """handler for file processing"""

        # Stuff Ansible needs to get started
        self._supports_check_mode = True
        self._supports_async = True

        # Boilerplate calling super method
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Rename url_username and url_password to user and password
        if "url_username" in self._task.args.keys():
            self._task.args["user"] = self._task.args["url_username"]
            del self._task.args["url_username"]
        if "url_password" in self._task.args.keys():
            self._task.args["password"] = self._task.args["url_password"]
            del self._task.args["url_password"]
        try:
            result.update(
                self._execute_module(
                    module_name="jenkins_script",
                    module_args=self._task.args,
                    task_vars=task_vars,
                )
            )
        except AnsibleAction as e:
            result.update(e.result)

        return result
