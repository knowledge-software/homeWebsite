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

baseURL = 'http://www.arcamax.com/zits'

zitsPage = urllib.urlopen(baseURL)
zitsText = zitsPage.read()
zitsPage.close()

# Try and process the page.
# The class should have been defined first, remember.
myparser = ImageTagParser()
myparser.parse(zitsText)

# Get the hyperlinks.
for anImage in myparser.get_hyperlinks():
	#print anImage
	if anImage.find("cgi-bin/news/pic/")>0:
		# strip off the '/cig-bin/news/' part
		anImage = '/'.join(anImage.split("/")[3:])
		foundToday = "http://www.arcamax.com/"+anImage  #anImage #
		print foundToday

import os

#print os.getcwd()
os.system( "curl -fs " + foundToday + " >zits.gif" )
print( "zits.gif" )

