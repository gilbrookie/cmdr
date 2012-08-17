
import aclip2

@aclip2.cmd("blog add")
def add_blog():
    print "adding new blog entry"

@aclip2.cmd("blog edit <id>")
def edit_blog(id):
    print "editing blog id %s" % id
