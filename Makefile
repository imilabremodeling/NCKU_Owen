
.PHONY: build-image push-image helm kustomize native

SERVER  =
COMMIT  =${shell git rev-parse --short HEAD}
VERSION ?=${COMMIT}
TYPE    ?=minikube
DEPLOY_GROUP=cnc2
REPO_NAME=imilabremodeling/campro

build-image:
	
	docker build --tag ${REPO_NAME}:${VERSION} .
	docker image tag ${REPO_NAME}:${VERSION} ${REPO_NAME}:${DEPLOY_GROUP} 	

push-image: build-image
	docker push ${REPO_NAME}:${VERSION}
	docker push ${REPO_NAME}:${DEPLOY_GROUP}

docker-lint:
	@echo "---------docker lint----------"

shellcheck:
	@echo "---------shell check----------"

test: shellcheck docker-lint 

native:
	@echo "---------kubectl yaml check -----------"

helm:
	@echo "---------helm yaml check -----------"

kustomize:
	@echo "---------kustomize yaml check -----------"
	@echo "--------- base -----------"
	@echo "--------- production -----------"
	@echo "--------- staging -----------"

k8s-yaml: native helm kustomize

bats:
	@echo "---------bats check-----------"
	sudo TYPE=${TYPE} bats -t tests/test.bats

k8s-test: k8s-yaml bats

                