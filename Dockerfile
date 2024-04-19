FROM mageai/mageai:latest

ARG PROJECT_NAME=uber-data-project

ARG USER_CODE_PATH=/home/${PROJECT_NAME}

COPY /pyspark_transformation_script ${USER_CODE_PATH}

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 
COPY requirements.txt ${USER_CODE_PATH}requirements.txt 

RUN pip3 install -r ${USER_CODE_PATH}requirements.txt
