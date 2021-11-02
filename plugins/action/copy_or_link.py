from ansible.errors import AnsibleAction
from ansible.plugins.action import ActionBase
from ansible.plugins.action.copy import ActionModule as CopyModule

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display

    display = Display()


class ActionModule(ActionBase):
    def __init__(self, *args, **kargs):
        super(ActionModule, self).__init__(*args, **kargs)
        self.__my_copy = CopyModule(*args, **kargs)

    def run(self, tmp=None, task_vars=None):
        """handler for file processing"""

        # Stuff Ansible needs to get started
        self._supports_check_mode = True
        self._supports_async = True

        # Boilerplate calling super method
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Determine the method of operation
        if self._connection.transport == "local":
            # Create a symlink to the destination
            self._task.args["state"] = "link"
            try:
                result.update(
                    self._execute_module(
                        module_name="file",
                        module_args=self._task.args,
                        task_vars=task_vars,
                    )
                )
            except AnsibleAction as e:
                result.update(e.result)
        else:
            # Force only applies to file module
            if "force" in self._task.args:
                del self.__my_copy._task.args["force"]
            result.update(self.__my_copy.run(task_vars=task_vars))

        return result
