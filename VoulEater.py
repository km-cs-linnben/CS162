# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word ")
user_word = user_word.upper()
disallowed_characters = "AEIOU"
for letter in disallowed_characters:
    # Complete the body of the for loop.
	user_word = user_word.replace(letter, "")
print(user_word)
