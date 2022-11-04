"""
Name: Ken Michna
Date: 5/4/2022

Question: In the code example above, rewrite the code so that if error “line number not in file”
occurs the program keeps asking for input until the user gets it right.

"""

# read a particular line from a file. User provides both the line
# number and the file name

while True:    #Begin loop for opening file. Resets if file name not found
    try:
        file_str = input( "Open what file: " )
        input_file = open(file_str)
        break
    except FileNotFoundError:
        print("The file", file_str ,"doesn't exist.")
        continue
    #the file closes here after the loop exits.It must be opened again. Why didnt I know that? So many hours wasted :(

file_len = 0    #Find how many lines are in file for comparison later,
for line in input_file:    # because I suck at efficient coding
    file_len += 1

while True:    #Begin loop asking for line number. Resets if line number entered is not an integer
    input_file = open(file_str)    #This line fixed my code after many hours of frustration. Lesson learned. 
    try:
        find_line_str = input( "Which line (integer): " )
        find_line_int = int(find_line_str) # potential user error

        line_count_int = 1
        if file_len < find_line_int or find_line_int < 0:    #outputs error messege if conditions not met. Resets loop to line 30
            print("Line {} of file {} not found".format(find_line_int, file_str))
            continue

        else:    #if number entered is valid then do this
            for line_str in input_file:    #for loop to find and print requested line of file
                if line_count_int == find_line_int:
                    print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
                    break
                line_count_int += 1
        
        input_file.close()    #Close file to make teacher happy.
        break
    
    except ValueError:    #restart loop in user enters anything besides an integer
        print("Line",find_line_str," Isn't a legal line number.") # 6, "six"
        continue

print("End of program.")