#!/bin/sh

WORK_DIR=/home/onyxia/work
CLONE_DIR=${WORK_DIR}/explainable-demo
ENV_DIR=${WORK_DIR}/explainable-env
# Clone course repository
REPO_URL=https://github.com/pedevineau/explainable-demo.git
git clone --depth 1 $REPO_URL $CLONE_DIR

pip install virtualenv
virtualenv $ENV_DIR
source ${ENV_DIR}/bin/activate

# Install additional packages if needed
REQUIREMENTS_FILE=${CLONE_DIR}/requirements.txt
[ -f $REQUIREMENTS_FILE ] && pip install -r $REQUIREMENTS_FILE && rm $REQUIREMENTS_FILE


# Remove course Git repository
#rm -r $CLONE_DIR

chown jovyan -R /home/jovyan/ # Otherwise jovyan has no rights on the local repo folder.
