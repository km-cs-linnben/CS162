

class piglet:
        def __init__(self, name, age):
                self.name = name
                self.age = age
                self.human_age = age*18
        def speak(self,sp_name):
                print(f"Oink OInk my name is {sp_name}")



charlotte = piglet("Charlotte",2)
charlotte.speak(charlotte)

