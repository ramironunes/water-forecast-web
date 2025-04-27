import os

from invoke import task
from invoke.context import Context

# 🏗️ Dynamically determine workspace and environment name
CURRENT_DIR = os.path.abspath(os.getcwd())
WORKSPACE = os.path.basename(os.path.dirname(os.path.dirname(CURRENT_DIR)))
PROJECT_NAME = os.path.basename(CURRENT_DIR).replace("-core", "")
CONDA_ENV_NAME = f"{PROJECT_NAME}-py313"
CONDA_SCRIPT = os.path.expanduser("~/miniconda/etc/profile.d/conda.sh")
CONDA_ENV = os.path.expanduser(f"~/w/{WORKSPACE}/envs/{CONDA_ENV_NAME}")

print(f"🌍 Detected workspace: {WORKSPACE}")
print(f"🐍 Conda environment: {CONDA_ENV}")


def conda_run(context: Context, command: str) -> None:
    """
    Runs a command inside the Conda environment, ensuring Conda is loaded first.
    """
    full_command = f"source {CONDA_SCRIPT} && conda activate {CONDA_ENV} && {command}"
    context.run(f"bash -c '{full_command}'", pty=True)


@task
def install_dependencies(context: Context) -> None:
    """
    Installs dependencies from environment.yml using Conda.
    """
    print("📦 Installing dependencies...")
    conda_run(
        context,
        f"conda env update --prefix {CONDA_ENV} -f environment.yml --prune",
    )
    print("✅ Dependencies installed successfully!")


@task
def install_precommit(context: Context) -> None:
    """
    Installs pre-commit and sets up the pre-commit hooks.
    """
    print("⚙️ Installing pre-commit...")
    conda_run(context, "pip install pre-commit")

    print("🔗 Setting up pre-commit hooks...")
    conda_run(context, "pre-commit install")

    print("✅ Pre-commit installed and hooks set up successfully!")


@task
def locks(context: Context) -> None:
    """
    Generates or updates lock files from environment.yml.
    """
    env_file = "environment.yml"
    lock_file = "environment.lock.yml"
    print(f"🔒 Generating lock file '{lock_file}' from '{env_file}'...")
    conda_run(context, f"conda-lock lock -f {env_file} --lockfile {lock_file}")
    print(f"✅ Lock file '{lock_file}' generated successfully!")


@task(pre=[install_dependencies, install_precommit, locks])
def setup(context: Context) -> None:
    """
    Installs dependencies and generates the lock file.
    """
    print("🚀 Running setup tasks...")
    conda_run(context, "echo '✅ Setup complete!'")
