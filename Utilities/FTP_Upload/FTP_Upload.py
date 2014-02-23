
'''
FTP UPLOAD
Jeff Thompson | 2014 | www.jeffreythompson.org

Basic example creating and uploading a file to a server using
the built-in 'ftplib' module.

Loads the connection settings from a separate file for security
reasons (see Settings.py for the format).

'''

from ftplib import FTP 				# for uploading to server
import os							# for basic file handling
from settings import settings		# load FTP settings from file (for security reasons)


# LOAD FTP SETTINGS FROM FILE
ftp_address = settings['ftp_address']
username = settings['username']
password = settings['password']
directory = settings['directory']
page_title = 'Download Bot'


# UPLOAD TO SERVER
# via: http://effbot.org/librarybook/ftplib.htm
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext.lower() in ('.txt', '.htm', '.html', '.css', '.js', '.php'):
        ftp.storlines('STOR ' + file, open(file))
    else:
        ftp.storbinary('STOR ' + file, open(file, 'rb'), 1024)


# BASIC HTML PAGE ELEMENTS
header = '''
<html>
<head>
	<title>''' + page_title + '''</title>
</head>
<body>

'''

footer = '''
</body>
</html>
'''


# CONNECT TO SERVER
ftp = FTP(ftp_address)			# create FTP object

print '+ Connecting to server...'
ftp.login(username, password)	# connect

print '+ Changing to "' + directory + '"...'
ftp.cwd(directory)				# change folders


# BUILD HTML CONTENT
body = ''
for i in range(100):
	body += '	<p>This is paragraph <a href="' + str(i) + '.html">' + str(i) + '</a>.</p>' + '\n'


# SAVE HTML TO FILE
print '+ Saving HTML file...'
with open('index.html', 'w') as output:
	output.write(header)
	output.write(body)
	output.write(footer)


# UPLOAD TO SEVER!
print '+ Uploading file to server...'
upload(ftp, 'index.html')

print 'ALL DONE!' + '\n\n'
ftp.quit()

