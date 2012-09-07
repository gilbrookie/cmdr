#
# Basic Makefile
#

# Install the source files into a temp location (using setup.py develop)
# And install any dependencies
init:
		python setup.py develop
		pip install -r requirements

# Cleaup files
clean:
		rm -rf *.pyc *.swp *.html

# Build the readme locally
readme:
		rst2html.py Readme.rst Readme.html
		python -m webbrowser -n "file://${PWD}/Readme.html"
		

