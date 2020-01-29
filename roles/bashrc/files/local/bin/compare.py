#! /usr/bin/env python
# Comapres two SWORD Bible modules for identical content
#
# This software, written by Greg Hellings, is distributed under the Modified Beerware License and
# is free for anyone to use for any purpose whatsoever.  No warantee, express or implied
# is given along with this program, nor is it guaranteed to be useful for any purpose whatsoever.
# If you find this code useful, feel free to tell me if you would like. If we are fortunate enough
# to meet and this was helpful to you, feel free to buy me a taco or a soda or something and tell
# me about it.
#
# Greg Hellings <greg.hellings@gmail.com>
import Sword
import sys

# Check we have sufficient options
if len(sys.argv) < 3:
	print 'Usage: %s <First Module> <Second Module>' % (sys.argv[0], )
	print 'Compares two SWORD Bible modules, verse by verse, to certify that the contents of each are identical.'
	sys.exit(-1)
# Warn if we have too many
if len(sys.argv) > 3:
	print 'Usage: %s <First Module> <Second Module>' % (sys.argv[0], )
	print 'WARNING: Only accepts two arguments, treating first two arguments as module names, ignoring the rest.'
	
# Grab the base SWORD manager
mgr = Sword.SWMgr()
# Get the two modules, provided they both exist - this is an advanced user tool, if these throw errors, too bad
original = mgr.getModule(sys.argv[1])
test     = mgr.getModule(sys.argv[2])
# Create the keys we will need so we can track - if original is not a Bible or Commentary, this will probably cause errors
key = Sword.VerseKey(original.CreateKey())
test.SetKey(key)
book = key.Book()

# Loop until one of the two modules throws an error, then exit
while original.Error() == '\x00' and test.Error() == '\x00':
	# Get the texts of each module and compare them
	oText = original.RenderText()
	tText = test.RenderText()
	if oText != tText:
		print 'Mismatch in %s\nOriginal text is**********:\n%s\nNew Text is*********:\n%s\n' % (key.getText(), oText, tText)
	# Increment the keys to the next verse, and provide feedback if we have finished comparing an entire canonical book
	original.increment()
	key = Sword.VerseKey(original.getKey())
	test.SetKey(key)
	if book != key.Book():
		print 'Checked up through %s' % (key.getText(),)
		book = key.Book()

# Alert the user where the comparison finished, in case we exited before the end of the Bible, indicating one of the modules
# might be incomplete
print 'Exited comparison at %s' % (key.getText(),)
