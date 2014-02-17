
'''
COUNT THINGS AND RECORD LOCATION IN TEXT
Jeff Thompson | 2014 | www.jeffreythompson.org

A more applied example - count the occurrences of things like names 
in the text, but also keep track of their location. This allows us 
to see a 'histogram' of where characters or ideas occur in a text.

CHALLENGE:
1. What kinds of words would be interesting to count? Can you create
   a robust regular expression to catch all variations (capitalized, etc)?
2. Can you compare the count of two or more terms? How might you visualize the results?
'''

import re


# VARIABLES
term = 'Frodo'																								# term to search for
input_filename = 'SourceTexts/LordOfTheRings_JRRTolkien.txt'	# file to load
words = []																										# blank list for all words
term_locations = []																						# blank list for locations of search term


# LOAD ALL WORDS INTO MASTER LIST
with open(input_filename) as input:
	for line in input:
		line = line.strip()									# removes newline (\n) characters
		words.extend(line.split())					# splits the line into words, adds to the master list of words

print 'Total # of words: ' + str(len(words))

# LOOK THROUGH WORD LIST, COUNT INSTANCES OF SEARCH TERM
for index, word in enumerate(words):		# use enumerate() so we can get the location too
	if word == term:											# if the word matches our search term...
		term_locations.append(index)				# ...append (add to) index the list of locations

print '# of times "' + term + '" appears: ' + str(len(term_locations))


# ok, that's cool but we can do more!


# WHICH PAGE HAS THE MOST INSTANCES OF THE TERM?
# a more useful example - our digital file doesn't include page numbers
# but we can guess what page the search term appears on using the estimate
# of 25 lines/page, 65 characters/line = ~1625 characters/page
# (via: http://answers.yahoo.com/question/index?qid=20080814062544AAJ01qr)

chars_per_page = 25 * 65		# average # of characters per page (see above)
char_position = 0						# keep track of where we are in the text char-by-char
page = 0										# which page does the character position translate to?
pages = {}									# dictionary to keep track of times the term appears per page

for word in words:
	if word == term:
		if page in pages.keys():
			pages[page] += 1										# if page is already stored, update count
		else:
			pages[page] = 1											# if NOT stored, create entry and set its value to 1
	
	char_position += len(word) + 1					# update position (+1 = space after word!)
	page = char_position / chars_per_page		# update page position

# create a list of the pages where the search term appears, sorted by how often the term appears
sorted_page_count = sorted(pages, key=pages.get)		# returns a list in ascending (low-high) order
most_page = sorted_page_count[-1]										# -1 gets last element in list!
most_page_count = pages[most_page]									# how many times does term appear on this page?
print '"' + term + '" appears most on page ' + str(most_page) + ' (' + str(most_page_count) + ' times)'

