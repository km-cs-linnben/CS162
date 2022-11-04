"""Demo some basic ideas around searching."""

# create some data
data = [i for i in range(1,11)]
#print(f"data: {data}")

# ask for value to find in data
# should validate user input!!!
user_input = int(input("Please enter a value to check in our list of data."))

# attempt to find the user's requested value in that data?

# This works fine with built-in functionality, but let's do the work ourselves
# if user_input in data:
#     print("True")
# else:
#     print("False")

# Check each value in the data list to see whether or not it is the value that we are looking for.
# result = False
result = None # how about if we want to know the index instead? ... Let's use None to indicate that the value was not found
for index, value in enumerate(data):
    if value == user_input:
        # print(f"user_input ({user_input}) is in the list at this position ({value})")
        # result = True
        result = index
        break # some variations based on what exactly we are looking for in our search...
        # could use a count variable to see ***how many times*** the value shows up in the list
    # else:
    #     print(f"user_input ({user_input}) is not in the list at this position ({value})")

# display whether search item was found or not
print(f"Result: {result}")
