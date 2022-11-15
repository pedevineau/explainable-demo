#!/bin/sh

SESSION=onyxia
WORK_DIR=/home/${SESSION}/work
CLONE_DIR=${WORK_DIR}/explainable-demo
ENV_DIR=${WORK_DIR}/explainable-env
# Clone course repository
REPO_URL=https://github.com/pedevineau/explainable-demo.git
git clone --depth 1 $REPO_URL $CLONE_DIR

pip install virtualenv p2j
p2j ${CLONE_DIR}/book.py -t ${CLONE_DIR}/book.ipynb
virtualenv $ENV_DIR
source ${ENV_DIR}/bin/activate

# Install additional packages if needed
REQUIREMENTS_FILE=${CLONE_DIR}/requirements.txt
[ -f $REQUIREMENTS_FILE ] && pip install -r $REQUIREMENTS_FILE && rm $REQUIREMENTS_FILE



# Remove course Git repository
#rm -r $CLONE_DIR

sudo chown ${SESSION} -R /home/${SESSION}/ # Otherwise onyxia user has no rights on the local repo folder.
