CONDA_INIT = eval "$$(conda shell.bash hook)"
ENV_FILE = environment.yml
ENV_NAME = project-template

.PHONY: build
build:
	conda info --envs | grep -q $(ENV_NAME) || conda env create -f $(ENV_FILE)
	conda env update --name $(ENV_NAME) --file $(ENV_FILE) --prune

.PHONY: setup
setup: build
	$(CONDA_INIT) && conda activate $(ENV_NAME) && inv setup

.PHONY: lint
lint:
	$(CONDA_INIT) && conda activate $(ENV_NAME) && ruff check . && mypy .

.PHONY: test
test:
	$(CONDA_INIT) && conda activate $(ENV_NAME) && pytest
