all: build run
remove:
	docker rm generator
	docker rmi badge-generator
remove-compose:
	docker rm badge-generator-py_badge-generator_1
	docker rmi badge-generator-py_badge-generator
build:
	docker build -t badge-generator .
run:
	docker run -i --name generator --env-file=.env badge-generator
compose:
	docker-compose up