
'''
INTRO TO REGULAR EXPRESSIONS
Jeff Thompson | 2014 | www.jeffreythompson.org

Regular expressions (also called regex) - strange-looking bits of code that 
can parse complex patterns of text - are difficult to get used to but are 
very powerful.  Below are some basic introductory examples to get you started!

As with all programming (but especially regex), there are lots of various and
sometimes better ways to accomplish the examples below. These are intended to
be as clear and readable as possible, perhaps at the expense of speed or
robustness :)

RESOURCES:
+ This cheat-sheet is an excellent starting place when learning regex
	- http://www.cheatography.com/davechild/cheat-sheets/regular-expressions/pdf
+ Also helpful:
	- http://net.tutsplus.com/tutorials/other/8-regular-expressions-you-should-know

CHALLENGE:
1. Look through the regular expression documentation and/or the web-based model listed
   above and create your own from scratch! Can you decide what to match, then write
   a regex to find that text?
'''


# import the regex module (it is not imported by default)
import re


# SOURCE SENTENCE (Shakespeare's 51st sonnet)
# (remember: triple-quotes keep quotes and line-breaks in a string intact)

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


# CONVERT SENTENCE TO LOWERCASE
# let's us match 'The' and 'the'
sentence = sentence.lower()


# FIND ALL INSTANCES OF THE LETTER 'T'
t = re.findall('t', sentence)		# returns a list of T's
print t													# could also use len(t) to get the # of T's


# FIND ALL WORDS STARTING WITH THE LETTER 'T'
# regular expressions use a series of symbols that form a 'pattern' that
# allows for very sophisticated text parsing - we use the letter 'r' in
# front of the pattern to tell Python how to interpret it

# below is a breakdown of our first example's pattern:
# \b = start looking at the start of a word
# t = letter t
# .* = greedy match = keep grabbing!
# ? = stop at first instance of next symbol
# \b = stop at end of word (ignores punctuation)
t_words = re.findall(r'\bt.*?\b', sentence)
print t_words


# FIND ALL WORDS THAT START WITH VOWELS
# [] means a list of values to match - here all the vowels upper- and lower-case
vowel_words = re.findall(r'\b[aeiuo].*?\b', sentence)
print vowel_words


# FIND ALL WORDS THAT END IN THE LETTER 'E'
# \w = word (kind of link \b, see: http://stackoverflow.com/a/11874899/1167783)
# * = greedy - catch everything up to letter 'e'
# e = letter 'e'
# \b = word boundary - ie: end of word
end_in_e = re.findall(r'\w*e\b', sentence)
print end_in_e


# GET ANY INSTANCE OF THE WORD 'I' FOLLOWED BY ANOTHER WORD
# () = capture only the part in the parentheses, letting us match but exclude spaces
# i = letter i
# \s = spaces (and tabs, line breaks, etc)
# .*? = greedy match until...
# \s = we hit another space
i_plus_word = re.findall(r'(i\s.*?)\s', sentence)
print i_plus_word

