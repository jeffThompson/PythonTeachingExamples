
'''
LETTER AND WORD COUNT
Jeff Thompson | 2014 | www.jeffreythompson.org

A simple first example: count the number of letters and words in a sentence.

'''

# SOURCE SENTENCE
# some text to work with - remember that we note strings with single- or double-quotes
sentence = 'It was the best of times, it was the worst of times'


# GET NUMBER OF CHARACTERS IN SENTENCE
# use the len() command to get the total number of letters, spaces, punctuation, etc
num_characters = len(sentence)
print num_characters

# or, format a little fancier!
# remember: we have to convert the # into a string using str()
print '# characters: ' + str(num_characters)


# GET LIST OF WORDS
# use the split() command to get a list of words
words = sentence.split()
print words										# notice 'words' is a list of all the words in the string!

# we can also split using an input 'argument' such as a comma
split_at_commas = sentence.split(',')
print split_at_commas

# how many words are there? use len() again to get the number of items in the list!
num_words = len(words)
print '# words: ' + str(num_words)

