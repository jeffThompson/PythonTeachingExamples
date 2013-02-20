# CREATE DICTIONARY OF WORDS
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# While looking for certain words can work if you know what you're
# looking for, sometimes you want to find patterns without knowing
# what's in the text!
#
# Here we use a structure called a 'dictionary' - this is like a list
# but only stores unique items (ie: no repeats) called 'keys'. Each
# key can have a 'value'.  In our case, we store words as the keys
# and their count as values.
#
# Included is also a commented-out method for recording only words over
# a certain length.  These words are called 'hexagraphs' and tend to
# weed out common and connective words (and, there, etc) and include
# meaningful words.

# CHALLENGE:
# 1. Load a text file and apply this process to the entire text
# 2. Create separate dictionaries - how would you divide the text? How can you
#    compare the dictionaries when done?


# sentence to parse (the Gettysburg Address, actually)
sentence = "Fourscore and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation or any nation so conceived and so dedicated can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field as a final resting-place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But in a larger sense, we cannot dedicate, we cannot consecrate, we cannot hallow this ground. The brave men, living and dead who struggled here have consecrated it far above our poor power to add or detract. The world will little note nor long remember what we say here, but it can never forget what they did here. It is for us the living rather to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us--that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion--that we here highly resolve that these dead shall not have died in vain, that this nation under God shall have a new birth of freedom, and that government of the people, by the people, for the people shall not perish from the earth."

# convert to lowercase (for better matching) and split into a list of words
sentence = sentence.lower()
words = sentence.split()

# create a blank dictionary and store words and their count
dictionary = {}						# dictionary is notated by { }
for word in words:					# go through all words in the sentence
	try:
		dictionary[word] += 1		# if word is already stored, increment count by 1
	except:
		dictionary[word] = 1		# if NOT stored, set its value to 1

# another version, storing only words above a certain length
# this method tends to weed out common words like 'the' and return more 'interesting' ones
'''
for word in words:
	if len(word) > 4:
		try:
			dictionary[word] += 1
		except:
			dictionary[word] = 1
'''

# how many unique elements are in the dictionary?
numUnique = len(dictionary)
print "# of unique words: " + str(numUnique)

# find the most common word!
# note there are some faster ways to do this, but those methods
# are much less readable (via: http://stackoverflow.com/a/12343826/1167783)
values = list(dictionary.values())					# make a list of the values (word counts)
keys = list(dictionary.keys())						# make a list of the keys (words)
maxCount = max(values)								# what is the maximum word count?
mostCommonWord = keys[values.index(maxCount)]		# get the word by the value
print "Most common word: " + str(mostCommonWord)
print "# of occurances:  " + str(dictionary[mostCommonWord])
