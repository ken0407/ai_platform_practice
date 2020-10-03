#!make

ci:
	docker image build -t training .
	docker run training make test
	make training

test:
	make format
	pytest -v -m ""

format:
	isort ai_platform_practice/*.py
	black -l 100 ai_platform_practice

local_training:
	gcloud ai-platform local train \
		--package-path ${TRAINING_PACKAGE_PATH} \
		--module-name ${MAIN_TRAINER_MODULE}

training:
	gcloud ai-platform jobs submit training iris_${COMMIT_SHA} \
		--job-dir ${JOB_DIR} \
		--package-path ${TRAINING_PACKAGE_PATH} \
		--module-name ${MAIN_TRAINER_MODULE} \
		--region ${REGION} \
		--runtime-version=${RUNTIME_VERSION} \
		--python-version=${PYTHON_VERSION} \
		--scale-tier ${SCALE_TIER}
