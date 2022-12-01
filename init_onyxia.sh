#!/bin/sh

# change the session name and the working directory if necessary
SESSION=onyxia
WORK_DIR=/home/${SESSION}/work

CLONE_DIR=${WORK_DIR}/explainable-demo
ENV_DIR=${WORK_DIR}/explainable-env
# Clone course repository
REPO_URL=git@github.com:pedevineau/explainable-demo.git
EXAMPLE_URL=git@github.com:pedevineau/school_meal_forecast_xgboost.git

git clone --depth 1 $REPO_URL $CLONE_DIR
git clone --depth 1 $EXAMPLE_URL ${CLONE_DIR}/example

# python3.7 is used for the sake of the demo on canteens, but it is not needed for the other source codes
# at this point install python3.7 and python3.7-distutils for your host. Example for debian/ubuntu below:
# sudo apt install python3.7 python3.7-distutils

python3.7 -m pip install virtualenv p2j
p2j ${CLONE_DIR}/frame.py -t ${CLONE_DIR}/frame.ipynb
python3.7 -m virtualenv $ENV_DIR
source ${ENV_DIR}/bin/activate

# Install additional packages if needed
REQUIREMENTS_FILE=${CLONE_DIR}/requirements.txt
REQUIREMENTS_EXAMPLE=${CLONE_DIR}/example/requirements.txt
python3.7 -m pip install -r $REQUIREMENTS_FILE
python3.7 -m pip install -r $REQUIREMENTS_EXAMPLE


# the last line is for onyxia
sudo chown ${SESSION} -R /home/${SESSION}/ # Otherwise onyxia user has no rights on the local repo folder.
