"""
This program does not work, it is for my reference only

"""

def write(self)-> None:
    with open(self.name, "w") as output_file:   #with auto closes file after
        output_file.write(self.name + "\n")   #write attributes from person object into text file
        output_file.write(str(self.age) + "\n")
        output_file.write(str(self.is_alive) + "\n")

def read(filename: str) -> Person:
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
    
    new_person = Person()   #creates a new person object
    new_person.name = lines[0][0:-1]   #reads lines from file and assigns them to new_person attributes
    new_person.age = lines[1][0:-1]

    return new_person