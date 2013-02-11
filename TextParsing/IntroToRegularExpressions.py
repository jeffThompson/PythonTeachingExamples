# INTRO TO REGULAR EXPRESSIONS
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# Regular expressions (also called regex) - strange-looking bits of code that 
# can parse complex patterns of text - are difficult to get used to but are 
# very powerful.  Below are some basic introductory examples to get you started!
#
# As with all programming (but especially regex), there are lots of various and
# sometimes better ways to accomplish the examples below. These are intended to
# be as clear and readable as possible, perhaps at the expense of robustness :)
#
# CHALLENGE:
# 1. Look through the regular expression documentation and/or the web-based model listed
#    above and create your own from scratch! Can you decide what to match, then write
#    a regex to find that text?


# the regex code is not imported automatically
import re

# using triple-quotes means anything between is part of the text, including line-breaks and quote-marks!
# here our source is Shakespeare's 51st sonnet
sentence = """Thus can my love excuse the slow offence
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
Towards thee I'll run, and give him leave to go."""

# find all letter 't'
t = re.findall("t", sentence)
print t

# find all words starting with 't'
# \W = word boundary (means we don't grab in the middle of a word)
# t = letter t
# .* = greedy match = keep grabbing!
# ? = stop at first instance of next symbol
# \W = stop at end of word (ignores punctuation)
tWords = re.findall("\Wt.*?\W", sentence)
print tWords

# capture t-words separate from the whitespace
# same as before, but only returns what's in the parentheses!
tWithoutSpaces = re.findall("\W(t.*?)\W", sentence)
print tWithoutSpaces

