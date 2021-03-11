.PHONY: init

GIT_HASH := $(shell git rev-parse --short HEAD)

SERVICE := "hsq"
IMAGE := "gcr.io/noobshack-164103/$(SERVICE)"

# Docker Image management
build:
	docker build --pull --build-arg GIT_HASH=$(GIT_HASH) -t $(IMAGE):$(GIT_HASH) .

tag: build
	docker tag $(IMAGE):$(GIT_HASH) $(IMAGE):latest

push: tag
	docker push $(IMAGE):latest
	docker push $(IMAGE):$(GIT_HASH)

test: tag
	docker run --rm -it -e FLASK_APP=$(FLASK_APP) -p 5000:5000 -e HSQ_CLIENT_ID=$(HSQ_CLIENT_ID) -e HSQ_CLIENT_SECRET=$(HSQ_CLIENT_SECRET) $(IMAGE):$(GIT_HASH)
