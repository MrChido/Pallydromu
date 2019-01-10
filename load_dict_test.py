"""This program loads the dictionary file as a list"""

import sys

def load(words):
	try:
		with open('words.txt') as in_file:
			print ("jolly good")

	except IOError as e:
		print ("{}\n Error opening {}. Program Terminated.".format(e, 'words.txt'))
		sys.exit(1)
