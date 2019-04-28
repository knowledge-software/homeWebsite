#!/usr/bin/python

# Print the required header that tells the browser how to render the text.
#print "Content-Type: text/plain\n\n"

# Initialize a few variables.
#first = "bob"
#middle = 7.5
#last = "marley"
#
#first,last = last,first

# Print the values.
#print "first:", first
#print "middle:", middle
#print "last:", last
#
# pysample.py: lives in the Page table and maps into cgi-bin/pysample.py
#
# reads /tmpl/pysample.tmpl and populates the following format tokens
#
#     %(today)s.
#     %(person)s
#     %(amount)f.2
#
import time, cgi

#
# This is a special test component that allows for debugging.  Comment out for final test.
import cgitb; cgitb.enable()

d = {
    'today' : time.asctime(),
    'person': "Web Person",
    'amount': 23.45
    }
#print ">>","yo!"
#tmpl = ""
#
#tmpl = file("../cgi-bin/pysample.tmpl").read()
#tmpl = "%(today)s.\n%(person)s\n%(amount)f.2"
#
print """\
Content-Type: text/html

<b><center>%(today)s<br>
HELLO WORLD</center>
</b>
""" % d # % cgi.test()
#%s
#print cgi.print_directory()
#print "<br>A <simple> phrase<br>"
#print cgi.escape("A <simple> phrase.")

import getpass, poplib

M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print j
