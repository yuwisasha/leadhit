build:
	docker compose build
up:
	docker compose up -d
down:
	docker compose down 
test:
	docker compose exec app poetry run pytest -v