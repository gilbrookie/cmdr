
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cmdr import Cmdr

app = Cmdr("blog_cli", prompt_str="==> ")

entries = []


@app.cmd("blog add")    # Full command
def add_blog():
    """Add a new blog entry"""
    print("adding new blog entry")
    entry = {}
    entry['title'] = input("Title: ")
    entry['text'] = input("Text: ")
    entry['type'] = input("Type [N]ote, [B]log")
    entry['timestamp'] = datetime.now()

    print(entry)
    entries.append(entry)

@app.cmd("blog edit")
def edit_blog(id):
    """This doesn't do anything"""
    print("editing blog id %s" % id)

app.start()
