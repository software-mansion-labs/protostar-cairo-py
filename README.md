# protostar_cairo_py

This is an internal package used by [Protostar](https://github.com/software-mansion/protostar).

```
         PROTOSTAR
          [Python]
             │
             ▼
      PROTOSTAR-CAIRO-PY
          [Python]
             │
             ▼
SOFTWARE-MANSION-LABS/CAIRO (fork)
           [Rust]
             │
             ▼
           CAIRO
           [Rust]
```
## Setting up the environment
1. Install a Python version management tool such as [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://github.com/asdf-vm/asdf).
1. Install Python 3.9.14.
1. Clone this repository.
1. Verify that the active Python version is python 3.9.14.
1. Create a virtual environment: `python -m venv .venv`.
1. Activate the environment: `source .venv/bin/activate`.
1. Upgrade pip: `pip install --upgrade pip`.
1. [Install Poetry](https://python-poetry.org/docs/#installation), which is the dependency manager used by this package.
1. Install project dependencies: `poetry install`.
1. Install Rust by following the instructions on [rust-lang.org](https://www.rust-lang.org/tools/install).
1. Test if everything works by building a wheel: `poe build`.
## Deploying
1. Update the git submodule: `poe sync`.
1. Release a package: `poe deploy`.