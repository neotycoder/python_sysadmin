#!/usr/bin/python

# Import CGI and CGITB
import cgi, cgitb

# Create a form object
form = cgi.FieldStorage()

# Get form data Full Name and Favorite TV Show
fullname = form.getvalue('fullname')
tvShow = form.getvalue('tvShow')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>TV Viewer Profile</title>"
print "</head>"
print "<body>"
print "<h2>Hello "+str(fullname) +"</h2>"
print "<p> Your favorite TV show is: "+str(tvShow)
print "</body>"
print "</html>"