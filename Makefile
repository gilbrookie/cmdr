PYTHON?=python

init:
		python setup.py develop
		pip install -r requirements

clean:
		rm -rf *.pyc *.swp *.html

readme:
		@python rst2html.py Readme.txt Readme.html
		@python -m webbrowser -n "file://{$PWD}/Readme.html"
		

