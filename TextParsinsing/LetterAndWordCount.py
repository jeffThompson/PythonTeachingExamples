# LETTER AND WORD COUNT
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
#

# this is our source sentence, stored in a variable called 'sentence'
# notice we differentiate the text from a number using quotes (single or double)
# in programming, text like this is called a 'string'
sentence = 'It was the best of times, it was the worst of times'

# get the total number of characters (letters, spaces, punctuation, etc)
numCharacters = len(sentence)		# len returns the # of chars in the string
print numCharacters					# print displays the value onscreen

# or, format a little fancier by combining values in the 'print' command
print '# characters: ' + str(numCharacters)		# one extra step: we have to convert the # into a string using str()

# get the total number of words
words = sentence.split(' ')			# split takes an argument so it knows where to split the string
print words							# notice 'words' is a list of all the words in the string!
numWords = len(words)				# use len() again to get the # of items in the list = # of words!
print '# words: ' + str(numWords)