"""
Filename: michna_kenneth_hangman.py
Author: Ken Michna
Date: 5/30/2022
CS161 Final Project

Description: A Game of Hangman
"""

#!/usr/bin/env python3

# Adapted from the MIT 6.0001 Word Game
# Released under CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode


# start of helper code
# -----------------------------------
# You will need to know how to use the helper functions
# so be sure to read the comments!

import random
import string
import pathlib


WORDLIST_FILENAME = "words.txt"


def load_words():
    """Return a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may take a while to
    finish.

    Returns:
        list: a list of strings
    """
    print("Loading word list from file...")

    # file is the absolute path to a file on disk
    file = pathlib.Path(pathlib.Path(__file__).parent) / WORDLIST_FILENAME

    # in_file represents a file on disk, we can use this to read the file's
    # contents
    in_file = open(file, "r")

    # line is the string read from in_file
    line = in_file.readline()

    # word_list is a list of strings made by splitting line on space characters
    word_list = line.split()

    print(len(word_list), "words loaded.")

    return word_list


def choose_word(word_list):
    """Choose a randome word from a list.

    Args:
        word_list (list): list of strings

    Returns:
        string: a random string from word_list
    """
    return random.choice(word_list)


# Load the list of words into the global variable WORDS so that it can be
# accessed from anywhere in the program
WORDS = load_words()

# -----------------------------------
# end of helper code


def is_word_guessed(secret_word: str, letters_guessed: list) -> bool:
    """Return whether or not the entire secret word has been guessed.

    Args:
        secret_word (string):  the word the user is guessing; assumes all
        letters are lowercase

        letters_guessed (list): a list of strings where each string is exactly
        one character (letter) that has already been guessed; assumes that all
        characters are lowercase

    Returns:
        boolean: True if all the letters of secret_word are in letters_guessed;
        False otherwise
    """
    for letter in secret_word:
        if letter in letters_guessed:
            solved = True
        else:
            solved = False
            break

    return solved


def get_guessed_word(secret_word: str, letters_guessed: list) -> str:
    """Build a string representing the word as the user has guessed it.

    Where the user has guessed a letter in the secret word, that letter should
    appear in the correct place in the returned string. Letters in the secret
    word that have not yet been guessed should be represented by a combination
    of an underscore-and-space ('_ ').

    Args:
        secret_word (string): the secret word the user is guessing

        letters_guessed (list): a list of strings where each string is exactly
        one character (letter) that has already been guessed; assumes that all
        characters are lowercase

    Returns:
        string: a string comprised of letters, underscores (_), and spaces
        representing the user's guess so far
    """
    
    guessed_list = []
    sw_letter_list = []

    
    for letter in secret_word:    #Creates a list of composed of 1 "_" for every letter in the secret word
        guessed_list.append("_ ")
    for letter in secret_word:    #Creates a list composed of each individual letter in the secret word
        sw_letter_list.append(letter)

    ind = 0    #Initialize a variable for index position
    for letter in sw_letter_list:    #Iterates through each letter in the secret word list
        if letter in letters_guessed:    #If that letter is in the list of guessed letters
            guessed_list[ind] = sw_letter_list[ind]    #Change the _ at the same index position in guessed_list to that letter 
            ind += 1    #Advance index position
        else:
            ind += 1

    new_word = "".join(guessed_list)    #create a new string of _ and letters out of completed guessed_list

    return new_word    #return that string


def get_available_letters(letters_guessed: list) -> str:
    """Build a sting containing all the still available letters.

    Available letters are those that have not yet been guessed.

    Args:
        letters_guessed (list): a list of strings where each string is exactly
        one character (letter) that has already been guessed; assumes that all
        characters are lowercase

    Returns:
        string: a string comprised of all the remaining letters which have not
        yet been guessed
    """
    
    abc_string = "abcdefghijklmnopqrstuvwxyz"    #now I know my abcs
    letters_avail_list = []    #Empty list of letters that have not been guessed

    for letter in abc_string:    #Iterates through abcs
        if letter in letters_guessed:    #Do nothing if letter is in list of already guessed letters
            pass
        else:
            letters_avail_list.append(letter)    #If that letter is not in the list of guessed letters, add to list of available letters
    
    letters_avail_string = "".join(letters_avail_list)    #Create a string out of list of available letters

    return letters_avail_string    #return list of available letters as a string

def get_score(secret_word: str,guesses_remain: int) -> int:
    """Returns score. Score = number of unique letters in word * number of guesses that remain"""
    unique_letters = set(secret_word)
    score = len(unique_letters) * guesses_remain

    return score


def hangman(secret_word):
    secret = secret_word
    guesses = len(secret)   #Final writeup says number of guesses should be the same as the amount of letters in word
    warnings = 3
    letters_guessed_list = []   #initialize list that will contain list of already guessed letters
    solved = False
    vowels = ["a","e","i","o","u"]

    print(f"\nWelcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret)} letters long.")
    print(f"You have {warnings} warnings left.")


    while guesses > 0 and solved == False:
        #Continues to loop as long as guesses and warnings still remain, and word has not been solved

        if warnings == False:    #Begin loop, first check if warnings are left
            guesses -= 1    #lose 1 guess
            warnings = 3    #reset warnings back to 3
            print("You got too many warnings, lose 1 guess")

        print("*"*12)
        print(f"You have {guesses} guess(es) left")
        print(f"Available letters: {get_available_letters(letters_guessed_list)}")


        # Guess entry suite. Will jump to guess analysis suite once user entry is valid
        valid = False
        while valid == False and warnings > 0:    # Will continue to loop as long as warnings still remain and entry has not been validated
            
            guess = str(input("Please guess a letter: "))

            if len(guess) == 1 and guess.isalpha() == True:
                valid = True    #Validates entry and exits loop
            elif len(guess) > 1:    #if user enters more than 1 character warnings reduced by 1
                warnings -= 1
                print(f"Enter 1 letter only. You have {warnings} warnings left. ")
            else:    #if user enters an integer or non alpha character, reduce warnings by 1
                warnings -= 1
                print(f"You have entered something other than a letter. You have {warnings} warnings left.")
        

        if warnings == False:    #If no warnings left after guess entry, jump back to begining of loop
            continue

        guess = guess.lower()    #lower case guess string
        

        #Guess analysis suite. Goes to here once a valid guess is entered
        if guess in letters_guessed_list:
            warnings -= 1
            print(f"You already guessed that letter! Lose 1 Warning")
            if warnings <= 0:
                continue
        elif guess in secret:
            print(f"Good guess!")
            letters_guessed_list.append(guess)    #Add letter to list of already guessed letters
            print(get_guessed_word(secret,letters_guessed_list))    #Print guessed letters of secret word
        else:
            letters_guessed_list.append(guess)    #Add letter to list of already guessed letters
            print(f"OOPS! That letter is not in my word!")
            print(get_guessed_word(secret,letters_guessed_list))    #Print guessed letters of secret word
            if guess in vowels:
                guesses -= 2    #Lose 2 points if wrong guess is a vowel
            else:
                guesses -= 1    #Otherwise lose 1 point
        

        solved = is_word_guessed(secret,letters_guessed_list)   #Check if word is solved, exit loop if True
    
    #Go here if word has been solved
    if guesses > 0:
        print("Congratulations! You guessed the word!")
        print(f"Your score is {get_score(secret,guesses)}")
    #Otherwise go here
    else:
        print("Sorry! YOU LOSE")
        print(f"The secret word was: \n{secret}")
        print("   |     ")
        print(" (x x)   ")
        print(" __|__   ")
        print("   |     ")
        print("  / \    ")
        print(" /   \   ")

      

if __name__ == "__main__":
    print(pathlib.Path(__file__).cwd())
    print(pathlib.Path(__file__).parent)

    ############################################################################
    # Now it is time to test your hangman function. Uncomment the two lines
    # below and run the program to play the game. Hint: You might want to pick
    # your own secret_word while you're testing. To do so, comment out the line:
    #
    # secret_word = choose_word(WORDS)
    #
    # and replace it with:
    #
    # secret_word = "secret"
    #
    # or any other word of your choosing. Be sure to replace the call to
    # choose_word and test the program again before submitting it.
    ############################################################################

    secret_word = choose_word(WORDS)
    hangman(secret_word)
