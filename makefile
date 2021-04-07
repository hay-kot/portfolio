setup:
	cd site && yarn install && \
	cd .. && \
	poetry install \

dev:
	docker-compose -f docker-compose.dev.yml -p dev-portfolio up --build

dev-local:
	cd site && yarn dev

publish:
	poetry run python ./article_processor/main.py