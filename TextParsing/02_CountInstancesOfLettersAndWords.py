
'''
COUNT INSTANCES OF LETTERS AND WORDS
Jeff Thompson | 2014 | www.jeffreythompson.org

Counting words can show patterns and themes in texts; here we count
vowels, then a more advanced example that counts words.

For this we use two important programming structures: if/else statements
and for loops. See the 'IfElse' and 'ForLoops' examples in the 'Basics'
folder for a complete explanation of how these work.

A more advanced example that counts only words over a certain length 
can be found in the 'CreateDictionary' example.

CHALLENGE:
1. Can you count the # of upper- and lower-case letters?
2. Can you count two or more words that seem meaningful in the source and compare
   the results automatically? 
   
'''

# IMPORT EXTRA FUNCTIONALITY
# needed for the last example
import re

# SOURCE SENTENCE
sentence = 'One ring to rule them all, one ring to find them, one ring to bring them all and in the darkness bind them.'


# CHECK IF SENTENCE CONTAINS COMMAS
# a very simple example
if ',' in sentence:
	print 'sentence contains commas!'


# this is great, but doesn't tell us very much - what if we want to note all instances of commas?


# FIND ALL COMMAS
# go through all the letters in the sentence, print every time we find a comma
for character in sentence:		# goes through the string character-by-character
	if character == ',':				# if the current character is a comma
		print 'comma!'


# also great, but what if we want to count the instances to get a total?


# COUNT ALL VOWELS
vowelCount = 0															# variable to store the count
sentence = sentence.lower()									# convert sentence to lowercase (so that 'A' and 'a' both match)
for c in sentence:													# iterate characters
	if c in 'aeiou':													# is the current character a vowel?
		vowelCount += 1													# increment the count!
print '# of vowels: ' + str(vowelCount)			# ...and print the results


# COUNT WORDS
# look for instances of a specific word in the sentence

# to do this, we first split sentence into a list of words
words = sentence.split()		# split at spaces into a list
print words									# print the list of words

# count instances of the word 'ring'
ring_count = 0															# like vowels, count instances of word
for word in words:													# go through all resulting words one-by-one
	if word == 'ring':												# if the current word is 'ring'
		ring_count += 1													# increment the count
print '# of rings: ' + str(ring_count)			# the results!


# note our method isn't perfect - if 'ring' is next to a comma or period, it
# will be listed at 'ring,' instead and will not match - we'll come back to
# this problem in the 'IntroToRegularExpressions' example.
