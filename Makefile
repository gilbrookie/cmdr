#
# Basic Makefile
#

# Install the source files into a staging location (using setup.py develop)
# And install any dependencies
init:
		pip install -r requirements.txt
		python setup.py develop

# Cleaup temp and compiled files
clean:
		rm -vrf *.pyc *.html

# Run the unittests
test:
		nosetests -v ./tests/

# run flake8 (pep8 + pyflakes) on tests and source only
pep8:
		@echo "\nRunning Flake8"
		flake8 -v --statistics --max-line-length=85 --exclude=*.pyc,*.git,*.rst --exit-zero tests/ cmdr/

travis: test pep8

# Build the readme locally
readme:
		rst2html.py Readme.rst Readme.html
		python -m webbrowser -n "file://${PWD}/Readme.html"

# remove the local staging files
uninstall:
		python setup.py develop -u

sphinx-docs:
		cd docs; make html
		python -m webbrowser -n "file://${PWD}/docs/_build/html/index.html"
# Generate sphinx documentation
docs: sphinx-docs
