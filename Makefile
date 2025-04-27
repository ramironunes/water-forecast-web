# Path to Conda initialization script
CONDA_SCRIPT = $(HOME)/miniconda/etc/profile.d/conda.sh

# Define the environment file and name
ENV_FILE = environment.yml
ENV_NAME = project-template-py313

# Define the workspace environment path dynamically
WORKSPACE_ROOT = $(shell dirname $(shell dirname $(shell pwd)))
WORKSPACE_NAME = $(shell basename $(WORKSPACE_ROOT))
WORKSPACE_ENV_PATH = $(HOME)/w/$(WORKSPACE_NAME)/envs/$(ENV_NAME)

.PHONY: build
build:
	@echo "🔧 Creating/updating Conda environment: $(ENV_NAME)..."
	conda info --envs | grep -q $(WORKSPACE_ENV_PATH) || conda env create -p $(WORKSPACE_ENV_PATH) -f $(ENV_FILE)
	conda env update --prefix $(WORKSPACE_ENV_PATH) --file $(ENV_FILE) --prune
	@echo "✅ Environment $(ENV_NAME) is up-to-date!"

.PHONY: setup
setup: build
	@echo "🚀 Running setup tasks..."
	bash -c "source $(CONDA_SCRIPT) && conda activate $(WORKSPACE_ENV_PATH) && inv setup"
	@echo "🎉 Setup completed successfully!"

.PHONY: lint
lint:
	@echo "🔍 Running code analysis..."
	bash -c "source $(CONDA_SCRIPT) && conda activate $(WORKSPACE_ENV_PATH) && ruff check . --fix && mypy ."
	@echo "✅ Code analysis completed!"

.PHONY: test
test:
	@echo "🧪 Running tests..."
	bash -c "source $(CONDA_SCRIPT) && conda activate $(WORKSPACE_ENV_PATH) && pytest"
	@echo "✅ Tests executed successfully!"
