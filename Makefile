PROJECT ?= kafka-producer-tool
PROJECT_VERSION ?= latest
export PROJECT
export PROJECT_VERSION

COMPOSE_FILE=docker/docker-compose.yml
DC=docker-compose -p ${PROJECT} -f ${COMPOSE_FILE}

.PHONY: build
build: ##@development Build containers. Needed only after changes in requirements.
build: args?= -f docker/Dockerfile
build:
	docker build --progress=plain -t ${PROJECT}:${PROJECT_VERSION} ${args} .

.PHONY: build-redpanda
build-redpanda: ##@development Build containers. Needed only after changes in requirements.
build-redpanda: args?= -f docker/redpanda.Dockerfile
build-redpanda:
	docker build --progress=plain -t redpanda-console:latest ${args} .

.PHONY: start
start: ##@development Start a flask-app instance.
	${DC} run -d application

.PHONY: redpanda-console
redpanda-console: ##@development Start a flask-app instance.
	${DC} run -d redpanda-console

.PHONY: stop
stop: ##@development Stop and remove containers created by up command.
	${DC} down --remove-orphans

.PHONY: application
application: ##@development
	${DC} up -d

.PHONY: shell
shell: ##@development Starts a bash shell.
	${DC} run --rm shell