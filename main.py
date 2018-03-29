# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mtan <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/29 13:07:31 by mtan              #+#    #+#              #
#    Updated: 2018/03/29 13:07:33 by mtan             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

############################################################################
#                             LIBRARIES
############################################################################

# To get arguments from command line
import sys
# To choose a random answer based on a given word length
import random


############################################################################
#                             DICTIONARIES
############################################################################

# Keep track of which letters have already been played
alpha_dict = {
	'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,	'f': 0,	'g': 0,	'h': 0,
	'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
	'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
	'y': 0, 'z': 0
}

############################################################################
#                             FUNCTIONS
############################################################################

# Initializing all necessary variables
def initialize_variables():
	d = {}
	answer = ""
	working = ""
	return d, answer, working

# Objective: Creating a dictionary with keys as length, and result an array of words.
def read_file_to_dict():
	d = {}
	# Note: argv[0] is the name of the file, args start from 1, 2, ..
	with open(sys.argv[1]) as f:
		for line in f:
			words = line.split()
			for word in words:
				length = len(word)
				# Note: d.keys() returns a list of all keys
				if length not in d.keys():
					d[length] = []
				d[length].append(word)
	return d

# Objective: Get a random word based on length
def get_my_answer():
	length = int(sys.argv[2])
	# Note: d[length] returns the array of words with "length" letters
	answer = random.choice(d[length])
	return (answer)

# Objective: Get the starting line to play Hangman
def get_working_line():
	working = ""
	length = int(sys.argv[2])
	for index in range(0, length):
		working = working + "_"
		if index < (length - 1):
			working = working + " "
	return (working)

# Objective: Try a letter, and show if it does
def try_move(answer, working, move):
	if alpha_dict[move] is 1:
		print("Letter {move} was played before. Try another letter!")
		return working
	working = working.split(" ")
	# Note: enumerate() creates a tuple of (index, char)
	for char in enumerate(answer):
		if char[1] is move:
			working[char[0]] = char[1]
			alpha_dict[letter] = 1
	working = " ".join(working)
	return working

############################################################################
#                             COMMANDS
############################################################################

# Simulate letter on cmd line
letter = sys.argv[3]

d = read_file_to_dict()

answer = get_my_answer()

working = get_working_line()

print("Answer: " + answer)

working = try_move(answer, working, letter)

print("Working:" + working)
