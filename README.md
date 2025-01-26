# Project Template

This repository serves as a template for projects, offering a structured setup with Conda, pre-commit hooks, and automation tools to ensure code quality and streamline development workflows.

---

## **Features**

- Environment management with Conda and `conda-lock` for dependency locking.
- Code quality checks with `ruff` and `mypy`.
- Pre-commit hooks for automated linting and formatting.
- Task automation using `Invoke` and `Makefile`.
- Ready-to-use structure for source code and tests.
- GitHub Actions workflows for CI/CD.

---

## **Requirements**

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Mamba](https://mamba.readthedocs.io/).
- `make` (optional but recommended for easier task management).

---

## **Setup Instructions**

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd project-template
   ```

2. Create and activate the environment:

   ```bash
   make setup
   ```

3. Verify the setup:
   ```bash
   make lint
   make test
   ```

---

## **Makefile Commands**

| Command      | Description                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| `make build` | Ensures the environment is created and updated with `conda`.                |
| `make setup` | Sets up the Conda environment, installs dependencies, and pre-commit hooks. |
| `make lint`  | Runs `ruff` and `mypy` to check code quality and type hints.                |
| `make test`  | Runs the test suite using `pytest`.                                         |

---

## **Pre-commit Hooks**

This project uses pre-commit hooks to ensure consistent code quality. Installed hooks include:

- `ruff` for linting and formatting.
- `mypy` for static type checking.

Hooks are installed automatically with `make setup`. To run them manually:

```bash
pre-commit run --all-files
```

---

## **Contributing**

1. Fork this repository.
2. Create a new branch (`git checkout -b fb-your-feature-name`).
3. Commit your changes with a meaningful message.
4. Push to the branch (`git push origin fb-your-feature-name`).
5. Open a pull request.

---
