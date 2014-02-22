
'''
FOR LOOPS
Jeff Thompson | 2014 | www.jeffreythompson.org

The 'for loop' is a very useful structure for going
through a list, repeating a process, and other repetitive
tasks. While the syntax of for loops can be ugly in
other languages, Python makes it much easier to understand!

'''

# GO THROUGH A LIST
# a simple but useful example - print the items in a list
rainbow = [ 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet' ]

for color in rainbow:		# just like if/else statements, use a colon and indent
	print color						# prints the colors of the rainbow!


# COUNT TO 10
# here we use the 'range()' command to count
# like in most programming languages, counting starts at 0 and
# runs to 1 less than the number listed

for i in range(10):		# print numbers 0-9
	print i


# RUNNING TOTAL
count = 0							# start the count at 0
for i in range(100):	# go through all #s from 0-99
	count += i					# add to count
print count						# print the result when done!


# ENUMERATE
# sometimes you want to go through a list, but also note
# the position (called the 'index') of an item - for this
# we use 'enumerate()'
baked_goods = [ 'donut', 'french bread', 'muffin', 'bagel' ]

for index, item in enumerate(baked_goods):		# get both position and item in list
	if index == 2:															# change third item (at index 2) of list
		baked_goods[index] = 'cookie'

print baked_goods															# print the changed list

