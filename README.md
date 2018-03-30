# Hangman
Who doesn't love Hangman? (Well, except the hanging man himself)

<img src="https://raw.githubusercontent.com/mgia/hangman/master/img/state.png" width="500" height="250">

## Overview

I built this project to supplement a course curriculum for HackHighSchool prepared by @KaiDrumm. For educational purposes, 
code is written in long but simpler form and commented generously to assist students.

The program:
- Reads from an input file and populates its word bank as a dictionary (a.k.a. hashtable)
- Chooses a random word, based on word length specified
- Runs a play loop, displaying current state
- If the player runs out of lives, game is over
<img src="https://raw.githubusercontent.com/mgia/hangman/master/img/failure.png" width="600" height="30">
- If all blanks are filled, player wins!
<img src="https://raw.githubusercontent.com/mgia/hangman/master/img/success.png" width="600" height="30">

## Run

Populate the input file with words to choose from.<br>
Next, run this command:

`python main.py`
