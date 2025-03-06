export PYTHONPATH=src

install:
	uv sync

build:
	uv build

lint:
	uv run ruff check .

test:
	uv run pytest -vv tests
