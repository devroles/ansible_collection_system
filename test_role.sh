#!/bin/bash
set -eux

MOLECULE="$(readlink -f "$(dirname "${0}")")/tests/molecule.yml"
# When invoking from tox, this will indicate the virtualenv to use that includes
# the necessary Python dependencies
if [ ! -z "${VIRTUAL_ENV}" ]; then
	set +xu
	source "${VIRTUAL_ENV}/bin/activate"
	set -xu
fi

# run all the Docker-based scenarios in a specific role
scenarios="$(find molecule/ -name 'molecule.yml' -exec grep '{}' -e '  name: docker' -l ';')"
for scenario_dir in "${scenarios}"; do
	scenario="$(basename "$(dirname "${scenario_dir}")")"
	molecule -c "${MOLECULE}" test -s "${scenario}"
done
