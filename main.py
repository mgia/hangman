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

# Notes:
# Some changes for Python v3
# 'raw_input' => 'input' 									(multiple lines)
# sys.stdout.write() => print(letter.upper(), end = " ")	(line 125)

############################################################################
#                             LIBRARIES
############################################################################

# To get arguments from command line
import sys

# To access file directory to check if file exists
import os

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
	word_bank = {}
	answer = ""
	working = ""
	return word_bank, answer, working

# Objective: Creating a dictionary with keys as length, and result an array of words.
def read_file_to_dict(word_bank):
	# Note: argv[0] is the name of the file, args start from 1, 2, ..
	filename = input("Input file name: ")
	# Note: To catch in the case file is typed wrongly, or does not exist
	if not os.path.exists(filename):
		print("Error: File incorrect, or not found, program exit")
		sys.exit()
	with open(filename) as f:
		for line in f:
			words = line.split()
			for word in words:
				length = len(word)
				# Note: word_bank.keys() returns a list of all keys
				if length not in word_bank.keys():
					word_bank[length] = []
				word_bank[length].append(word)
	return word_bank

# Objective: Get a random word based on length
def get_my_answer(answer, word_bank):
	length_str = ("Specify length: ")
	length = int(length_str)
	# Note: Try / except allows you to handles errors
	try:
		# Note: word_bank[length] returns the array of words with "length" letters
		answer = random.choice(word_bank[length])
	# Note: Catches for when there is no key, i.e. no words to choose)
	except KeyError:
		print("No words for this specified length. Program exit")
		sys.exit()
	return (answer, length)

# Objective: Get the starting line to play Hangman
def get_working_line(working, length):
	for index in range(0, length):
		working = working + "_"
		if index < (length - 1):
			working = working + " "
	return (working)

# Objective: Try a letter, and show if it does
def try_move(answer, working, move, lives):
	if alpha_dict[move] is 1:

		# README KAI: This print appears above the terminal clear cmd,
		# so it will not be seen in current state. Potential use if
		# you want to create move history
		print("Letter '{}' is repeated".format(move.upper()))

		# Note: In case of double letter, return life to player
		lives = lives + 1
		return working, lives
	# Note: .split(" ") cuts the string by the spaces to create elements
	working = working.split(" ")
	# Note: enumerate() creates a tuple of (index, char)
	for char in enumerate(answer):
		if char[1] is move:
			working[char[0]] = char[1]
	# Note: Set the letter to 'Not Available'
	alpha_dict[move] = 1
	# Note: Create the new current state with the letter filled in.
	working = " ".join(working)
	return working, lives

# Objective: Check for proper exit condition
def exit_success(working):
	for char in working.split(" "):
		if char > 'z' or char < 'a':
			return (0)
	return (1)

# Objective: Print the available alphabets for any given state
def print_letters():
	print("--------------------------")
	for letter in alpha_dict:
		if alpha_dict[letter] is 0:
			sys.stdout.write(letter.upper() + " ")
	sys.stdout.write('\n')
	print("--------------------------")

# Objective: Main while loop to play each turn
def play(answer, working, lives):
	while not exit_success(working):
		# Note: Catches case for no more lives
		if lives is 0:
			print("Failure! Poor man... RIP")
			print("Answer: " + answer)
			sys.exit()
		# Note: 'Refreshes' terminal for a clean state output
		sys.stdout.write("\033[H\033[2J")
		# Note: Potential for UI Visualizer
		print("Current state: {}".format(working))
		print("Number of lives left: " + str(lives))
		print("Available:")
		print_letters()
		move = input("Letter: ")
		if len(move) > 1:
			print("Error: One letter at a time")
		else:
			try:
				working, lives = try_move(answer, working, move, lives)
				lives = lives - 1
			except KeyError:
				print("Error: invalid letter")
	print("Success! You saved the man. Good job!")
	print("Answer: " + answer)

############################################################################
#                             COMMANDS
############################################################################

# Initialize your variables
word_bank, answer, working = initialize_variables()

# Using a file as input, create a dictionary with (len, array of words)
word_bank = read_file_to_dict(word_bank)

# Choose a word based on word length
answer, word_length = get_my_answer(answer, word_bank)

# Using the same word length, create the corresponding working state
# i.e. "pie" become "_ _ _"
working = get_working_line(working, word_length)

# Number of lives
lives = 10

# Game loop
play(answer, working, lives)
