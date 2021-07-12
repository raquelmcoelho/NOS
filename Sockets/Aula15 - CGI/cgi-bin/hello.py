#!/usr/bin/python

import cgitb, cgi
cgitb.enable()

form = cgi.FieldStorage()

nome = form.getvalue('nome')

print("Content-type:text/html\r\n\r\n")
print('Hello, ', nome)

