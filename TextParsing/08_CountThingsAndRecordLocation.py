# COUNT THINGS AND RECORD LOCATION IN TEXT
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# A more applied example - count the occurrences of things
# like names in the text, but also keep track of their overall
# location. This allows us to see a 'histogram' of where
# characters or ideas occur and where they do not.
#
# CHALLENGE:
# 1. What kinds of words would be interesting to count? Can you create
#    a robust regular expression to catch all variations (capitalized, etc)?
# 2. Can you compare the count of two or more terms? How might you visualize the results?


import re													# regex for matching words

lookFor = "Frodo"											# look for instances of the character Frodo in LOTR
inputText = "SourceTexts/LordOfTheRings_JRRTolkien.txt"		# input text to read
frodo = []													# create a blank list, add items per line
totalCount = 0												# count of instances of the word (set to 0 for now)

# first, we merge the text into one big long string, then split that
# into roughly page-length chunks - this gives us better stats on the
# flow of the book
fullText = ""
file = open(inputText)

pages = []
for line in file:
	fullText += line
file.close()

# grab page-length chunks (source: http://answers.yahoo.com/question/index?qid=20080814062544AAJ01qr)
pageSize = 25 * 65 									# average 25 lines/page at 65 chars/line
for start in range(0, len(fullText), pageSize):		# run through text from pos 0 - end in pageSize steps!
	pages.append(fullText[start:start+pageSize])	# add an entry to the list of the specified size

# open file and read line-by-line
for page in pages:
	instancesOfWord = re.findall("Frodo", page)		# find all instances of the word and return as a list
	totalCount += len(instancesOfWord)				# add the length of the list (# of words matched) to our overall count
	frodo.append(len(instancesOfWord))				# add a new record in the list - each line from the file will have a different value

# get some stats from our results
numPages = len(frodo)								# of pages in the file
peakCount = max(frodo)								# max value from the list of word instances
peakIndex = frodo.index(peakCount)					# location of the max value in the list

print "# of pages in file:  " + str(numPages)
print "Total count of word: " + str(totalCount)
print "Most freq occur:     " + str(peakCount) + " times (index: " + str(peakIndex) + ")"

print "\nMOST FREQ PAGE:"
print pages[peakIndex]

print "\nWORD COUNT PER PAGE:"
print frodo