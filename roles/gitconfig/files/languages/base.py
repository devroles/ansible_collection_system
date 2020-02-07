import os
from abc import ABC, abstractmethod
from contextlib import contextmanager
from subprocess import run
from tempfile import TemporaryDirectory


class Base(ABC):
    def __init__(self):
        self.home = os.curdir

    @abstractmethod
    def check(self):
        pass

    def run_command(self, command):
        """
        Runs the command, returns the RC value.

        :param command: An list, just as one might enter on the command line,
        that includes the executable and all the arguments
        :returns: The return code of the execution.
        """
        cp = run(command)
        return cp.returncode

    @contextmanager
    def mk_tmp_checkout(self):
        mirror = TemporaryDirectory()
        try:
            print("pre-commit: Making a checkout of the index")
            run(['git',
                 'checkout-index',
                 '--prefix={}/'.format(mirror.name),
                 '-af'])
            # If mirror.name is long-lived, you need to delete the changes here
            # git diff-index --cached --name-only --diff-filter=D -z HEAD |
            # (cd ${MIRROR} && xargs -0 -rm -f --)
            # Then rsync them to the final destination
            # rsync -rlpgoDO --size-only --delete ${MIRROR}/ ${FINAL_DEST}
            self.old_path = os.getcwd()
            os.chdir(mirror.name)
            yield
        finally:
            os.chdir(self.old_path)
            mirror.cleanup()
