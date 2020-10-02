#!make
include .env

test:
	pytest -v -m ""

local_training:
	gcloud ai-platform local train \
		--package-path $TRAINING_PACKAGE_PATH \
		--module-name $MAIN_TRAINER_MODULE

training:
	export -e $(cat .env) | xargs ; gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir ${JOB_DIR} \
		--package-path ${TRAINING_PACKAGE_PATH} \
		--module-name ${MAIN_TRAINER_MODULE} \
		--region ${REGION} \
		--runtime-version=${RUNTIME_VERSION} \
		--python-version=${PYTHON_VERSION} \
		--scale-tier ${SCALE_TIER}
