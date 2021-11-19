#!/usr/bin/env python

import subprocess
import sys
import re


class Toolbox:
    def __init__(self, name="toolbox"):
        self.name = name

    @property
    def boxen(self):
        box_p = subprocess.run(
            ["toolbox", "list", "-c"], stdout=subprocess.PIPE, text=True, check=True
        )
        box_p_lines = box_p.stdout.strip().split("\n")
        # First line of outpt is headers
        if len(box_p_lines) > 0:
            box_p_lines = box_p_lines[1:]
        # Fields are separated by 2 or more spaces
        all_boxes = [re.split(r"\s{2,}", n) for n in box_p_lines]
        # We only care about the name and state of it
        box_list = [{"name": m[1], "state": m[3]} for m in all_boxes]
        return box_list

    @property
    def existing(self):
        return list(map(lambda x: x["name"], self.boxen))

    @property
    def running(self):
        return list(
            map(
                lambda x: x["name"],
                filter(lambda y: y["state"] == "running", self.boxen),
            )
        )

    def create(self):
        if self.name in self.existing:  # Idempotence!
            return False, "Exists"
        create_p = subprocess.run(
            ["toolbox", "-vv", "create", self.name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if create_p.returncode == 0:
            return True, ""
        else:
            return False, create_p.stdout

    def run(self):
        if self.name in self.running:
            return False, "Running"
        run_p = subprocess.run(
            ["toolbox", "enter", self.name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            input="",
            text=True,
        )
        if run_p.returncode == 0:
            return True, ""
        else:
            return False, run_p.stdout


def main():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
            "name": {"required": True, "type": str},
            "running": {"required": False, "type": bool},
        }
    )
    tb = Toolbox(module.params["name"])
    # Create the toolbox, first
    create_changed, answer = tb.create()
    if not create_changed and answer != "Exists":
        module.fail_json(msg=f"Error encountered:\n{answer}")
    # If we don't want it running, just exist now
    if not module.params["running"]:
        module.exit_json(changed=create_changed)
    # If we want it running, then do this
    if module.params["running"]:
        running_changed, answer = tb.run()
        if not running_changed and answer != "Running":
            module.fail_json(msg=f"Error starting toolbox:\n{answer}")
    changed = create_changed or running_changed
    module.exit_json(changed=changed)


# Testing
def testing():
    tb = Toolbox()
    print("Toolboxen")
    for f in tb.boxen:
        print(f["name"], f["state"])
    print("\nExisting")
    for f in tb.existing:
        print(f)
    print("\nRunning")
    for f in tb.running:
        print(f)

    print("\nCreate should fail")
    tb.name = "This doesn't work"
    yes, answer = tb.create()
    print(yes, answer)
    assert not yes

    print("\nCreate should no-op, at least for me")
    tb.name = "fedora-toolbox-34"
    print(tb.existing)
    yes, answer = tb.create()
    print(yes, answer)
    assert not yes
    assert answer == "Exists"

    print("\nCreate and run something new")
    tb.name = "tbtest"
    yes, answer = tb.create()
    assert yes
    assert answer == ""
    yes, answer = tb.run()
    assert yes
    assert answer == ""
    print("\nCheck idempotency")
    yes, answer = tb.run()
    assert not yes
    assert answer == "Running"


if sys.argv[-1] != "do_test":
    main()
else:
    testing()
