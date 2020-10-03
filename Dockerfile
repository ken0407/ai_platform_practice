FROM python:3.7-buster
ENV BUCKET_NAME=${BUCKET_NAME} JOB_DIR=${JOB_DIR} TRAINING_PACKAGE_PATH=${TRAINING_PACKAGE_PATH} \
    MAIN_TRAINER_MODULE=${MAIN_TRAINER_MODULE} REGION=${REGION} RUNTIME_VERSION=${RUNTIME_VERSION} \
    PYTHON_VERSION=${PYTHON_VERSION} SCALE_TIER=${SCALE_TIER}

RUN git clone https://github.com/ken0407/ai_platform_practice.git && cd ai_platform_practice && pip install .[test]
WORKDIR ai_platform_practice