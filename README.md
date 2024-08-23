# Sandbox: Sort

A place to store my brain solution to testing and related handy things.

## Usage

### Using venv

```shell
python3 -m venv ./venv_sandboxsort
```

```shell
source ./venv_sandboxsort/bin/activate
```

### Installing Sandbox Sort Requirements

```shell
pip install -r requirements_dev.txt
```

### Testing

![Tests](https://github.com/UnicodeTreason/sandboxsort/actions/workflows/tests.yml/badge.svg)

Run all tests

```shell
pytest
```

Run all unittest tests

```shell
python3 -m unittest discover -s tests/
```

Run a specific unittest test

```shell
python3 -m unittest tests/algorithms/test_bogo.py
```

### Running

Run module

```shell
python3 -m sandboxsort
```

Run specific sort

```shell
python3 ./sandboxsort/algorithms/sort_bogo.py
```
