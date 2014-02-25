
'''
PARSE CSV - BETTER
Jeff Thompson | 2014 | www.jeffreythompson.org

But what about data with commas? The answer is really complicated, so
we use Python's built-in CSV module :)

This is a great example of extracting and cleaning up data - we start
with a bigger data set, then pull out just a part that we want to
look at. For some tasks, Microsoft Excel is also a very helpful tool.

QUOTECHAR
The 'quotechar' argument for the CSV module lets us specify what data
that includes comments is contained in - generally, this is double-
quotes, like this:

	1,"New York, New York",8244910

Notice that New York, New York is in quotes, since the city name includes
a comma.

CHALLENGE:
1. 	Try printing just one part of each listing, for example the population.
2. 	Try extracting one part of the data, collecting it, and saving the
	results to a new file.
'''

import csv												# load Python's CSV module

input_file = 'SourceData/LargestCitiesUS.csv'			# file to read

with open(input_file) as input:							# open the file
	
	data = csv.reader(input, quotechar = '"')			# parse data using csv module
	
	for index, listing in enumerate(data):				# go through the data line-by-line
		if index != 0:									# skip header (the first line in the file)
			print listing								# print each data listing (note it's a list)

