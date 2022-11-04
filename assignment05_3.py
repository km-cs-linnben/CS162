"""
Name: Ken Michna
Date: 5/4/2022

Question: In the code example above, rewrite the code so that if error “bad file name” occurs the 
program keeps asking for input until the user gets it right.

"""

# read a particular line from a file. User provides both the line
# number and the file name
while True:
    try:
        file_str = input( "Open what file: " )
        input_file = open(file_str)
        break
    except FileNotFoundError:
        print("The file", file_str ,"doesn't exist.")
        continue

try:
    find_line_str = input( "Which line (integer): " )
    find_line_int = int(find_line_str) # potential user error
    line_count_int = 1

    for line_str in input_file:
        if line_count_int == find_line_int:
            print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
            break
        line_count_int += 1
    else:
        # get here if line sought doesn't exist
        print("Line {} of file {} not found".format(find_line_int, file_str))
    input_file.close()

except ValueError:
    print("Line",find_line_str," Isn't a legal line number.") # 6, "six"
    print("End of the program")

print("End of program.")