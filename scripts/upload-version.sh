#!/usr/bin/env bash

export DELTA_ML_COMMON_VERSION=$1
source venv/bin/activate
python3 setup.py sdist
# TODO add api token to login account
twine upload dist/DeltaML-commons-${DELTA_ML_COMMON_VERSION}.tar.gz
deactivate