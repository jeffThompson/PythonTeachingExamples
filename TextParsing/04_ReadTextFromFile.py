
'''
READ FROM TEXT FILE
Jeff Thompson | 2014 | www.jeffreythompson.org

Reading text from a file is very easy with Python (much easier than other
languages like Java). Here we go through a file line-by-line and count
the number of gendered pronouns in the text (something that would be
VERY time consuming and error-prone by hand).

Look in the 'SourceTexts' folder for more example source files.
'''

import re										# load some extra code for easier pronoun matching


# VARIABLES
filename = "SourceTexts/TimeMachine.txt"		# file to load - use a full path or store locally

lines = []										# empty list to store lines from the file
word_count = 0									# variables to keep track of # of words, gendered pronoun counts
male_count = 0
female_count = 0
neutral_count = 0


# READ FILE, COUNT PRONOUNS!
with open(filename) as input:		# opens the file (see note at bottom)**

	# go through file line-by-line using a for loop
	for line in input:
		line = line.lower()			# convert to lowercase so we match 'She' and 'she'

		# get all pronouns from the line
		# (since findall() returns a list, the length of that list is the # of matching pronouns!)
		male = re.findall('he|him|his|himself', line)		# the '|' means OR
		male_count += len(male)								
	
		female = re.findall('she|her|hers|herself', line)
		female_count += len(female)
	
		neutral = re.findall('it|its|itself', line)
		neutral_count += len(neutral)

		word_count += len(line.split())						# split line into words, add # of words to overall count


# PRINT THE RESULTS!
print '# of words in file: ' + str(word_count)
print 'Male pronouns:      ' + str(male_count)
print 'Female pronouns:    ' + str(female_count)
print 'Neutral pronouns:   ' + str(neutral_count)


'''
**OTHER WAY TO READ A FILE
You may also see files read as two separate lines:

input = open(filename)
input.close()

BUT: if you forget to close the file you're reading, it can
cause problems, so the syntax used in this example is
safer, especially for new programmers! :)
'''

