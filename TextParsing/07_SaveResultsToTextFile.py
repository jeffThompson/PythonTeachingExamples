
'''
SAVE RESULTS TO TEXT FILE
Jeff Thompson | 2014 | www.jeffreythompson.org

Programming is very useful for 'cleaning up' data, but if we
can't save the results into a file our efforts don't get us
too far, especially if parsing takes a long time!

This is basically the same as reading in a file, but we specify
either 'w' to write to a file, or 'a' to append (add to).

The example below removes all vowels from an input text! :)
'''

# IMPORT REGEX
import re


# VARIABLES
input_filename = 'SourceTexts/Sonnet51.txt'		# input filename
output_filename = 'SonnetWithoutVowels.txt'		# output filename
output_text = ''								# blank string to build output text


# GO THROUGH INPUT TEXT, REMOVE VOWELS
with open(input_filename) as input:
	for line in input:
		line = re.sub(r'[AEIOUaeiou]', '', line)	# replace vowels with... blanks!
		output_text += line							# add new text to output


# WRITE RESULTS TO FILE!
with open(output_filename, 'w') as output:
	output.write(output_text)

