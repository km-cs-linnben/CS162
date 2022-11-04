# Given a string of text
# If the parenthese are matched incorrectly, return False
# Otherwise, return True

def check_parenthesis(text):
    # Base case, no parenthesis ""
    if text == "" or ("(" not in text and ")" not in text):
        return True
    # recursive case
    # get rid of other characters
    # create a function that get rid of other characters.
    text = trim_char(text)
    print(text)
    if text[0] == "(" and text[-1] == ")":
        print(text)
        return check_parenthesis(text[1:-1])
    else:
        return False

def trim_char(text):
    # get rid of the non-"(" on the left hand side.
    for char in text:
        if char == ")":
            break
        if char != "(":
            char_index = text.index(char)
            text = text[char_index+1:]
        else:
            break

     # get rid of the non-")" on the left hand side.
    for char in text[::-1]:
        if char == "(":
            break
        if char != ")":
            text = text[:-1]
            # char_index = text.index(char)
            # text = text[:char_index+1]
        else:
            break
    return text
 
text = "Y(ukkaabcWille())y"
print(check_parenthesis(text))