# LETTER AND WORD COUNT
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# A simple first example: count the number of letters and words in a sentence.
#
# CHALLENGE:
# 1. Can you get the average word length? Hint: split by words, then count length and average


# this is our source sentence, stored in a variable called 'sentence'
# notice we differentiate the text from a number using quotes (single or double)
# in programming, text like this is called a 'string'
sentence = 'It was the best of times, it was the worst of times'

# get the total number of characters (letters, spaces, punctuation, etc)
numCharacters = len(sentence)		# len returns the # of characters in the string
print numCharacters					# print displays the value onscreen

# or, format a little fancier by combining values in the 'print' command
print '# characters: ' + str(numCharacters)		# one extra step: we have to convert the # into a string using str()

# get the total number of words
words = sentence.split(' ')			# split takes an argument so it knows what characters to look for to split the string
print words							# notice 'words' is a list of all the words in the string!

numWords = len(words)				# use len() again to get the # of items in the list = # of words!
print '# words: ' + str(numWords)