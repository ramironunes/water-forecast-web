from invoke import task
from invoke.context import Context


@task
def install_dependencies(context: Context) -> None:
    """
    Installs dependencies from environment.yml using Conda.
    """
    print("Installing dependencies...")
    context.run(
        "conda env update -n project-template -f environment.yml --prune",
        pty=True,
    )
    print("Dependencies installed successfully!")


@task
def install_precommit(context: Context) -> None:
    """
    Installs pre-commit and sets up the pre-commit hooks.
    """
    print("Installing pre-commit...")
    context.run("pip install pre-commit", pty=True)

    print("Setting up pre-commit hooks...")
    context.run("pre-commit install", pty=True)

    print("Pre-commit installed and hooks set up successfully!")


@task
def locks(context: Context) -> None:
    """
    Generates or updates lock files from environment.yml.

    Generates a lock file 'environment.lock.yml' based on the current
    environment.yml.

    """
    env_file = "environment.yml"
    lock_file = "environment.lock.yml"
    print(f"Generating lock file '{lock_file}' from '{env_file}'...")
    context.run(f"conda-lock lock -f {env_file} --lockfile {lock_file}", pty=True)
    print(f"Lock file '{lock_file}' generated successfully!")


@task(pre=[install_dependencies, install_precommit, locks])
def setup(context: Context) -> None:
    """
    Installs dependencies and generates the lock file.
    """
    print("Setup complete!")
