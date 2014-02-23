
'''
PARSE CSV - BETTER
Jeff Thompson | 2014 | www.jeffreythompson.org

But what about data with commas? The answer is really complicated, so
we use Python's built-in CSV module.

CHALLENGE:
1. Try printing just one part of each listing, for example population.

'''

import csv												# load Python's CSV module

input_file = 'SourceData/LargestCitiesUS.csv'			# file to read

with open(input_file) as input:							# open the file
	data = csv.reader(input, quotechar = '"')			# parse data using csv module
	for index, listing in enumerate(data):				# go through the data line-by-line
		if index != 0:									# skip header (the first line in the file)
			print listing								# print each data listing (note it's a list)

