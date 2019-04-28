#!/usr/bin/python
#

import sgmllib
#####################################
class TableTagParser(sgmllib.SGMLParser):
    "A simple parser class."

    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        "Initialise an object, passing 'verbose' to the superclass."

        sgmllib.SGMLParser.__init__(self, verbose)
        self.tableCount = 0;

    def start_img(self, attributes):
        "Process a hyperlink and its 'attributes'."

        for name, value in attributes:
            if name == "src":
                print value

	def start_table(self, attributes):
		self.tableCount = self.tableCount + 1
		if self.tableCount == 6:
			print attributes

	def do_table(self, attributes):
		self.tableCount = self.tableCount + 1
		if self.tableCount == 6:
			print attributes
			

#####################################

import urllib
import sgmllib

baseURL = 'http://forecast.weather.gov/MapClick.php?CityName=White+Plains&state=NY&site=OKX'

noaaPage = urllib.urlopen(baseURL)
noaaText = noaaPage.read()
noaaPage.close()

# Try and process the page.
# The class should have been defined first, remember.
myparser = TableTagParser()
myparser.parse(noaaText)

# Get the hyperlinks.
#for anImage in myparser.get_hyperlinks():
#	if anImage.find("newspics/")>0:
#		# strip off the '/cig-bin/news/' part
#		anImage = '/'.join(anImage.split("/")) # [3:])
#		foundToday = anImage #"http://www.arcamax.com/"+anImage
#		print foundToday

#import os

##print os.getcwd()
#os.system( "curl -fs " + foundToday + " >noaa.gif" )
#print( "noaa.gif" )

