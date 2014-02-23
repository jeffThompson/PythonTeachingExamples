
'''
PARSE CSV FILE - SIMPLE
Jeff Thompson | 2014 | www.jeffreythompson.org

The most common data file is called CSV or 'comma-separated values',
which separates columns of data by commas. For example:

	date,location,temperature,wind_speed
	12-24-2013,Atlanta,48,12

In this example, we split a line of CSV data into constituent 
values. Note that this is a simple example: "real-world" data
will often include commas within the data, like this:

	location
	"Atlanta, Georgia"

This would get split into TWO items, since the quote will get split
too! For how to deal with this, see the next example.

CHALLENGE:
1. 	Find a "real-world" CSV file somewhere online (try Data.gov) and
    parse the file - can you extract a single column and average it
    across the entire file?
'''

line = '12-24-2013,Atlanta,48,12'	# line of data to read
data = line.split(',')				# split into list at the commas

date = data[0]						# since we know the order of the data in each line...
loc = data[1]						# we can access each value from the split list
temp = data[2]
wind = data[3]

print 'Date:        ' + str(date)	# print the results!
print 'Location:    ' + str(loc)
print 'Temperature: ' + str(temp)
print 'Wind:        ' + str(wind)

