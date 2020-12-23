PY_VER=py38
VENV=env
CODE_DIRS=dicom_phi_check tests
LINE_LEN=120

style: 
	autoflake -r -i --remove-all-unused-imports --remove-unused-variables $(CODE_DIRS)
	isort $(CODE_DIRS) --line-length $(LINE_LEN) 
	autopep8 -a -r -i --max-line-length=$(LINE_LEN) $(CODE_DIRS) 
	black --line-length $(LINE_LEN) --target-version $(PY_VER) $(CODE_DIRS)

types:
	pyright $(CODE_DIRS) -p pyrightconfig.json

test:
	$(VENV)/bin/python3 -m pytest tests

quality: 
	black --check *.py --line-length=120
	flake8 *.py

init:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -e .[dev]

check:
	$(MAKE) style
	$(MAKE) types
	$(MAKE) test
