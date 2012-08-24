
from datetime import datetime

from aclip2 import application

app = application.Application("blog_cli")

@app.cmd("blog add")    # Full command
def add_blog():
    """Add a new blog entry"""
    print "adding new blog entry"
    title = raw_input("Title: ")
    text = raw_input("Text: ")
    type = raw_input("Type [N]ote, [B]log")

    print title
    print text
    print type
    print datetime.now()


@app.cmd("blog edit <id>")
def edit_blog(id):
    print "editing blog id %s" % id



app.start()
