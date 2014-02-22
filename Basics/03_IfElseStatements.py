
'''
IF/ELSE STATEMENTS
Jeff Thompson | 2014 | www.jeffreythompson.org

A basic structure that allows different code to be
executed depending on the result of a comparison.

INDENT!
If/else statements are followed by a colon. The code
to be executed must be indented so Python can know
what code is what. For example:

if 0 < 1:					# if statement with colon
	print 'true!'		# indented code is executed if true
else:
	print 'false!'

OPERATORS
>			greater than
<			less than
>=		greater than or equal to
<=		less than or equal to
==		equal to (note, this is different than a single =)
!=		not equal to
in		keyword to check if an item is in a list

'''

# COMPARE TWO NUMBERS
num_peanuts = 30
num_almonds = 120

if num_peanuts > num_almonds:		# note the colon
	print 'more peanuts!'					# note the indentation!
else:														# next statement is un-indented
	print 'more almonds!'


# COMPARE IF TWO STRINGS ARE EQUAL
my_name = 'Jeff'
another_name = 'Jeff'

if my_name == another_name:
	print 'we both have the same name!'


# MULTIPLE CONDITIONS
# we can compare multiple conditions using 'or' and 'and'
# (note: 'elif' is the Python version of 'else if' from other languages)
weather = 'rain'
if weather == 'rain' or weather == 'snow':
	print 'bring your umbrella!'
elif weather == 'clear':
	print 'should be nice today, leave the umbrella at home!'
else:
	print 'probably should check the weather report...'

# similar example, using 'and'
my_age = 51
my_nationality = 'American'
min_age = 35
req_nationality = 'American'

if my_age >= min_age and my_nationality == req_nationality:
	print 'you can run for president!'


# CHECK IF ITEM IS IN LIST
birds = [ 'parrot', 'cardinal', 'woodpecker' ]
bird = 'parrot'
if bird in birds:
	print bird + ' is in the list!'

# this also works to check if a string is in another one
# (this is because strings are actually lists in Python)
color = 'green'
sentence = 'the grass is always greener on the other side'
if color in sentence:
	print 'found ' + color + ' in the sentence!'

