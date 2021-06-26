setup:
	cd site && yarn install && \
	cd .. && \
	poetry install \

dev:
	cd site && yarn dev

publish:
	poetry run python ./article_processor/main.py