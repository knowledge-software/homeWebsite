#!/usr/bin/python
#

import sgmllib
#####################################
class ImageTagParser(sgmllib.SGMLParser):
    "A simple parser class."

    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."

        sgmllib.SGMLParser.__init__(self, verbose)
        self.hyperlinks = []

    def start_img(self, attributes):
        "Process a hyperlink and its 'attributes'."

        for name, value in attributes:
            if name == "src":
                self.hyperlinks.append(value)

    def get_hyperlinks(self):
        "Return the list of hyperlinks."

        return self.hyperlinks

#####################################

import urllib
import sgmllib

baseURL = 'http://www.gocomics.com/foxtrot'

thePage = urllib.urlopen(baseURL)
theText = thePage.read()
thePage.close()

# Try and process the page.
# The class should have been defined first, remember.
myparser = ImageTagParser()
myparser.parse(theText)

# Get the hyperlinks.
for anImage in myparser.get_hyperlinks():
	# print anImage
	if anImage.find("picayune.uclick.com")>0:          # looking for: http://picayune.uclick.com/comics/ft/2008/ft080713.
		# strip off the '/cig-bin/news/' part
		#anImage = '/'.join(anImage.split("/")[3:])
		foundToday = anImage #
		# print "**This is it! ++>" + foundToday

import os

#print os.getcwd()
os.system( "curl -fs " + foundToday + " >foxtrot.gif" )
print( "foxtrot.gif" )

