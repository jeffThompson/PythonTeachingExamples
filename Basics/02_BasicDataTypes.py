
'''
BASIC DATA TYPES IN PYTHON
Jeff Thompson | 2014 | www.jeffreythompson.org

Python is much kinder about data types than many
other programming languages. You can easily interchange
between letters, numbers, and sentences. However, it will 
be helpful to understand the basics and how to switch 
between them. 

Variables are values that can be assigned and updated. Declare
a variable by name, using something descriptive that tells
what it is or does. While spaces are not allowed in variable
names, you can use _ to make names more readable.

'''

# NUMBERS
# numbers can either be integers (whole numbers like 0, 4, or 365)
# or floating-point (decimals, like 3.14)
# numbers can be positive or negative too!

year = 2014								# example of an integer
fav_num = 3								# concise is sometimes better, so long as it's understandable...
approximate_pi = 3.14			# example of a float

# you can print numbers onscreen like this
print year


# BASIC MATH
# we can create new variables by doing basic math operations
# on our existing variables
# plus = +, minus = -, multiply = *, and divide = /

two_years_from_now = year + 2
print two_years_from_now

double_favorite_number = fav_num * fav_num
print double_favorite_number

# sometimes we want to update a variable
fav_num += 1							# this adds 1 to the variable...
fav_num = fav_num + 1			# ...which is the same as this!


# you can use parentheses to set the order of operations. Remember
# PERMDAS from basic algebra? Parentheses, exponential, radical,
# multiplication, division, addition, subtraction :)
mult_first = 2 + 3 * 4
print mult_first

add_first = (2 + 3) * 4
print add_first


# STRING 
# a string is a set of letters, such as a sentence
# strings are noted with either single- or double-quotes
first_name = 'Jeff'
last_name = "Thompson"

# you can combine strings using the + sign
full_name = first_name + ' ' + last_name		# notice we add a space between the words?
print full_name


# PRINTING STRINGS AND NUMBERS
# sometimes you want a label printed with a number - to do
# this we have to convert the number to a string
print 'The year is ' + str(year) + '.'


# BONUS
# what happens if we multiply a string?
print 'more ' * 20

# sometimes you want blank spaces - using the special '\n' character
# you can make them without needing multiple 'print' commands
print '\n\n\n' + 'this text has three blank lines before it, two after it' + '\n\n'


# LISTS
# a group of items is called a list, contained in [ ] with items separated
# by commas; unlike many other languages, Python lets you combine different
# data types into a single list
dwarfs = [ 'Doc', 'Dopey', 'Bashful', 'Grumpy', 'Sneezy', 'Sleepy', 'Happy' ]
print dwarfs

fibonacci = [ 1, 1, 2, 3, 5, 8, 13, 34, 55, 89, 144 ]
print fibonacci

# we can access items in the list using the 'index', or position
# (like most programming languages, the first item is at position 0)
print fibonacci[0]

# we can also change items in the list this way
fibonacci[0] = 100
print fibonacci

