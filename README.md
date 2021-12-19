### Tests and linters status

[![hexlet-check](https://github.com/EvilMadSquirrel/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EvilMadSquirrel/python-project-lvl2/actions/workflows/hexlet-check.yml)
[![Pytest](https://github.com/EvilMadSquirrel/python-project-lvl2/actions/workflows/pytest.yml/badge.svg)](https://github.com/EvilMadSquirrel/python-project-lvl2/actions/workflows/pytest.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/7039217e4b390cc65991/maintainability)](https://codeclimate.com/github/EvilMadSquirrel/python-project-lvl2/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/7039217e4b390cc65991/test_coverage)](https://codeclimate.com/github/EvilMadSquirrel/python-project-lvl2/test_coverage)

## Gendiff
### console utility for file comparison:
- compares JSON and YAML files
- possible result format: plain, tree or json
- can be used as a console utility or imported as a module

### Installation:

```bash
pip install --user git+https://github.com/EvilMadSquirrel/python-project-lvl2.git
```

## Usage
### as a console utility:

```bash
gendiff -h
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output
```

### as a module:
```python
from gendiff import generate_diff

diff = generate_diff("file1_path", "file2_path", "format")

print(diff)
```

## Examples of work

### flat and nested file format, tree output:
[![asciicast](https://asciinema.org/a/456864.svg)](https://asciinema.org/a/456864)

### flat and nested file format, flat output:
[![asciicast](https://asciinema.org/a/457096.svg)](https://asciinema.org/a/457096)

### nested file format, JSON output:
[![asciicast](https://asciinema.org/a/457175.svg)](https://asciinema.org/a/457175)

### questions and suggestions:
[Email me :)](minichev.s.l@gmail.com)