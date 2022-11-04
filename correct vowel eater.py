word_without_vowels = ""
word = input("enter a word: ")
word = word.upper()

for letter in word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter =="O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
        
print (word_without_vowels)
