# SAVE RESULTS TO TEXT FILE
# Jeff Thompson | 2013 | www.jeffreythompson.org
#
# Programming is very useful for "cleaning up" data, but if we
# can't save the results into a file our efforts don't get us
# too far, especially if parsing takes a long time.
#
# CHALLENGE:
# 1. How might you strip a column of data from a CSV file?
# 2. Can you build an automatic text-remixer that loads a source file
#    and re-organizes it into something else?

import re										# import regular expressions

inputFile = "SourceTexts/Sonnet51.txt"			# input and output files
outputFile = "SonnetWithoutVowels.txt"

source = open(inputFile)						# open source file

for line in source:								# read line-by-line
	line = re.sub("[AEIOUaeiou]", "", line)		# replace all vowels with nothing!
	with open(outputFile, "a") as file:			# open and append to file ("a" means add to end)
		file.write(line)						# write data!

source.close()									# be sure to close your input file!
												# no need to close output file when using the above method