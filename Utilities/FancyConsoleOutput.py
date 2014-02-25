
'''
FANCY CONSOLE OUTPUT
Jeff Thompson | 2013 | www.jeffreythompson.org

Instead of line after line when printing updates on
long processes, format into a single line that updates
itself!

NOTE: this will only work in some consoles - Sublime Text,
for example, does not work! :(

'''

import sys
import time

print '\nFANCY CONSOLE OUTPUT:'
for i in range(0,1000):							# go through lots of #s
	sys.stdout.write('\rIteration %i' % i)		# print the result
	sys.stdout.flush()							# finish printing to console
	time.sleep(0.01)							# wait 100th sec so we can see the results

print ''										# clear to a new line when done