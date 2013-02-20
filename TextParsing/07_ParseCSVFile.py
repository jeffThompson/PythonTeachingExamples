# PARSE CSV FILE
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# The most common data file is called CSV or 'comma-separated values',
# which separates columns of data by commas. For example:
#
#    date,location,temperature,wind_speed
#	 12-24-2013,Atlanta,48,12
#
# In this example, we split a line of CSV data into constituent values.
#
# CHALLENGE:
# 1. Find a "real-world" CSV file somewhere online (try Data.gov) and
#    parse the file - can you extract a single column and average it
#    across the entire file?


line = "12-24-2013,Atlanta,48,12"	# line of data to read
data = line.split(',')				# split at commas!

date = data[0]						# since we know the order of the data in each line
loc = data[1]						# we can access each value from the split list
temp = data[2]
wind = data[3]

print "Date:        " + str(date)	# print the results!
print "Location:    " + str(loc)
print "Temperature: " + str(temp)
print "Wind:        " + str(wind)

# what about commas in the data?
# for example, if instead of "Atlanta" we wanted to list "Atlanta, Georgia" - to
# accomodate this we generally put items with commas in quotes; however that means
# our split method will still split up the city and state :(

import csv														# use Python's CSV module!
inputFile = "SourceTexts/LargestCitiesUS.csv"					# file to read

whichLine = 0													# count lines as we go
with open(inputFile, 'rb') as input:							# open file
	file = csv.reader(input, delimiter=',', quotechar='"')		# read using csv; set delimiter and quote character
	for line in file:											# go through line-by-line
		# optionally skip the first line, since it has header data...
		if whichLine != 0:
			print line											# print a list of split values
		whichLine += 1											# increment line count

# note: if we wanted to read a regular string into the CSV module, we 
# need to do a little hack: put the string into [ ]
# for example:
#   line = csv.reader([line], delimiter=',', quotechar='"')