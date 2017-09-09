ECS_URL = "193635214029.dkr.ecr.eu-central-1.amazonaws.com/dunai"

build:
	docker build -t dunai .

run: | build
	docker run --rm --name dunai -it dunai

deploy: | build
	docker tag dunai ${ECS_URL}:latest
	docker push ${ECS_URL}:latest

