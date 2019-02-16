TOP_DIR ?= $(shell git rev-parse --show-toplevel)
INSTALL_DIR ?= $(TOP_DIR)/venv

install: $(INSTALL_DIR)
	. $(INSTALL_DIR)/bin/activate; \
	python setup.py --quiet install

$(INSTALL_DIR): $(INSTALL_DIR)/bin/activate
$(INSTALL_DIR)/bin/activate: requirements.txt
	test -d $(INSTALL_DIR) || virtualenv $(INSTALL_DIR)
	. $(INSTALL_DIR)/bin/activate; \
		pip install -r requirements.txt --process-dependency-links $(PIP_FLAGS); \
		pip install flake8==2.4.0 $(PIP_FLAGS)
	touch $(INSTALL_DIR)/bin/activate

test: lint test_nolint
test_nolint: install
	. $(INSTALL_DIR)/bin/activate; \
	python manage.py test tests

# Runs test coverage report
coverage: lint install
	. $(INSTALL_DIR)/bin/activate; \
		coverage run --source='.' manage.py test tests; \
		coverage report

# Removes build files in working directory
clean_working_directory:
	rm -rf ./build ./dist ./django_wellknown.egg-info ./.coverage;

# Removes sqlite db created for tests
clean_test_database:
	rm -rf db.sqlite3;

# Full clean
clean: clean_test_database clean_working_directory
	rm -rf $(INSTALL_DIR)

# Lint the project
lint: clean_working_directory
	. $(INSTALL_DIR)/bin/activate; \
	find . -type f -name '*.py' -not -path '$(INSTALL_DIR)/*' | xargs flake8

# Auto-format the project
format: clean_working_directory
	find . -type f -name '*.py' | xargs flake8 | sed -E 's/^([^:]*\.py).*/\1/g' | uniq | xargs autopep8 --experimental -a --in-place
