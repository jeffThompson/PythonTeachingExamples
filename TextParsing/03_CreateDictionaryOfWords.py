
'''
CREATE DICTIONARY OF WORDS
Jeff Thompson | 2013 | www.jeffreythompson.org

If you know what you want to count, the previous example might
work great, but sometimes you want to find patterns without knowing
what's in the text!

Here we use a structure called a 'dictionary' - this is like a list
but only stores unique items (ie: no repeats) called 'keys'. Each
key can have a 'value'.  In our case, we store words as the keys
and their count as values.

Included is also a commented-out method for recording only words over
a certain length.  These words are called 'hexagraphs' and tend to
weed out common and connective words (and, there, etc).
'''

# SENTENCE TO PARSE (the Gettysburg Address, actually)
# here we use three quotes (same as multiline comments) to ensure ' or " in
# the text don't mess things up
sentence = '''Fourscore and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation or any nation so conceived and so dedicated can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field as a final resting-place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But in a larger sense, we cannot dedicate, we cannot consecrate, we cannot hallow this ground. The brave men, living and dead who struggled here have consecrated it far above our poor power to add or detract. The world will little note nor long remember what we say here, but it can never forget what they did here. It is for us the living rather to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us--that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion--that we here highly resolve that these dead shall not have died in vain, that this nation under God shall have a new birth of freedom, and that government of the people, by the people, for the people shall not perish from the earth.'''


# EXTRACT WORDS INTO LIST
sentence = sentence.lower()						# convert all letters to lowercase (so words like 'And' and 'and' match)
sentence = sentence.replace(',.?!-', ' ')		# replace all punctuation with spaces (for better splitting)
words = sentence.split()						# split into a list


# GO THROUGH ALL WORDS, ADD TO DICTIONARY!
dict = {}										# create blank dictionary
for word in words:								# go through all words in the list
	if word in dict.keys():
		dict[word] += 1							# if word is already stored, increment count by 1
	else:
		dict[word] = 1							# if NOT stored, create entry and set its value to 1

# another version, storing only words above a certain length
# this method tends to weed out common words like 'the' and 'and'
'''
for word in words:
	if len(word) > 4:
		if word in dict.keys():
			dict[word] += 1
		else:
			dict[word] = 1
'''

# PRINT THE DICTIONARY (don't do this for a really long text!)
# print dict


# HOW MANY UNIQUE WORDS ARE IN THE SENTENCE?
num_unique_words = len(dict)							# just like a list!
print '# of unique words: ' + str(num_unique_words)		# print the result


# GETTING VALUES FROM THE DICTIONARY
# we can get the count for a particular word (such as 'nation') like this:
nation_count = dict['nation']
print '# of times the word "nation" appears: ' + str(nation_count)


# WHAT IS THE MOST COMMON WORD?
# note there are some faster ways to do this, but the code is much less readable
# (for a fancier example, see: http://stackoverflow.com/a/12343826/1167783)
keys = list(dict.keys())								# make a list of the keys (words)
values = list(dict.values())							# make a list of the values (word counts)
max_count = max(values)									# what is the maximum word count?
most_common_word = keys[values.index(max_count)]		# get the word by the value

print 'Most common word: "' + str(most_common_word) + '"'
print '# of occurances: ' + str(dict[most_common_word])

