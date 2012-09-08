#
# Basic Makefile
#

# Install the source files into a staging location (using setup.py develop)
# And install any dependencies
init:
		python setup.py develop
		pip install -r requirements.txt

# Cleaup temp and compiled files
clean:
		rm -vrf *.pyc *.html

# Run the unittests
test:
		nosetests -v ./tests/

# run flake8 (pep8 + pyflakes) on tests and source only
pep8:
		flake8 --max-line-length=85 --exclude=*.pyc,*.git,*.rst tests/ cmdr/

# Build the readme locally
readme:
		rst2html.py Readme.rst Readme.html
		python -m webbrowser -n "file://${PWD}/Readme.html"
		
# remove the local staging files 
uninstall:
		python setup.py develop -u
