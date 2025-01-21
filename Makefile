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

.PHONY: start
start: ##@development Start a flask-app instance.
	${DC} run application

.PHONY: stop
stop: ##@development Stop and remove containers created by up command.
	${DC} down --remove-orphans

.PHONY: application
application: ##@development
	${DC} up -d