install:
	poetry install

uninstall:
	pip uninstall hexlet-code

gendiff:
	poetry run gendiff --h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
