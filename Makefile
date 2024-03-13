docker-build-start:
	docker compose build
	docker compose up -d

docker-build-restart:
	docker compose down --remove-orphans
	docker compose build
	docker compose up -d

release:
	docker build -t compas/mock-aspu:v0.1 .