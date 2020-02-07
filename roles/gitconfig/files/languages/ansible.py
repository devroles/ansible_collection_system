from os import listdir, curdir
from os.path import join, isdir, exists
from .base import Base


class Ansible(Base):
    def check(self):
        molecule = join(curdir, "molecule")
        if not isdir(molecule):
            return False
        for scenario in listdir(molecule):
            if scenario != "shared" and \
               exists(join(molecule, scenario, "molecule.yml")):
                with self.mk_tmp_checkout():
                    print("pre-commit: Running molecule lint -s ", scenario)
                    rc = self.run_command(["molecule", "lint", "-s", scenario])
                return rc
        return 0
