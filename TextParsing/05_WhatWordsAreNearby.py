
'''
WHAT WORDS ARE NEARBY
Jeff Thompson | 2014 | www.jeffreythompson.org

Similar to our previous example that counted all unique words
using a dictionary structure, we can expand that idea a bit
to store the context in which we find certain words.

In other words: what words are most likely to come before and
after the word "love" in Shakespeare?

SET
For this example, we'll use a new data structure called a
'set'. A set is sort of like a list, except it only stores
unique items. If you try to add an item to a set that's already
been stored, it ignores the addition.

WHY DO THIS?
A simple reason is that it's just interesting. We can see
which words have the fewest connectors, or look for novel
findings like the example above.

This can also be expanded into what is called a Markov Chain,
which allows us to simulate the writing of an author! This
is used for things like spam bots, and can produce very
convincing text without any human intervention!

CHALLENGE:
1. Try loading from a file instead.
2. Can you research Markov Chains and expand our example
to create one? Hint: we need to not just add the connecting
words, but also their frequency. For this, you'll need
nested dictionaries.

'''

# import the 'Pretty Print' module, so our resulting
# dictionary prints in a readable format :)
import pprint


# VARIABLES
words = []			# list for words
nearby = {}			# dictionary for word, plus the previous/next words

sentence = '''Thus can my love excuse the slow offence
Of my dull bearer when from thee I speed:
From where thou art why should I haste me thence?
Till I return, of posting is no need.
O! what excuse will my poor beast then find,
When swift extremity can seem but slow?
Then should I spur, though mounted on the wind,
In winged speed no motion shall I know,
Then can no horse with my desire keep pace.
Therefore desire, (of perfect'st love being made)
Shall neigh, no dull flesh, in his fiery race;
But love, for love, thus shall excuse my jade-
Since from thee going, he went wilful-slow,
Towards thee I'll run, and give him leave to go.'''


# CLEAN UP A BIT, SPLIT INTO LIST OF WORDS
sentence = sentence.lower()
words = sentence.split()


# GO THROUGH WORD LIST, ADD TO DICTIONARY
# (use enumerate() so we can keep track of the index too)
for index, word in enumerate(words):
	
	# get previous and next words - here we use a 'try/except'
	# statement to catch errors (like trying to get the previous
	# word from the first word in the list)
	try:
		previous_word = words[index - 1]
		next_word = words[index + 1]
	except IndexError:						# except can have no argument, or catch specific errors
		pass								# pass just means skip and keep going

	# add to dictionary...
	if word in nearby.keys():				# if already stored...
		nearby[word].add(previous_word)		# use add() to add items to a set
		nearby[word].add(next_word)			# add next word too
	else:
		nearby[word] = set( previous_word )	# if not stored, create a new set with the previous word
		nearby[word].add(next_word)			# then add next word


# DONE!
pprint.pprint(nearby)	# print in a way that's easier to read

