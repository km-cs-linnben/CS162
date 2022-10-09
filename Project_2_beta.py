"""
Ken Michna
Project 1

Tested every available menu option for every menu and submenu with car running and in accessory mode.

WEEK 2 Version with test functions
"""

class Car:
    """Class defining a car object."""

    def __init__(self,make="Geo",model="Metro",engine="i3",trans="Auto",drivetrain="4WD",doors=2,color="Puke yellow"):
        self.make = make
        self.model = model
        self.engine = engine
        self.trans = trans
        self.drivetrain = drivetrain
        self.doors = doors
        self.color = color
        self.ign_status = "off"
        self.window_status = "up"
        self.wiper_status = "off"
        self.radio = 90
        self.gear_status = "P"
        self.drive_status = "2WD"
        self.test_val = 1   #this is for testing the class methods.
    
    def __str__(self):
        """Prints vehicle information."""

        return f"Make: {self.make}\n"\
        f"Model: {self.model}\n"\
        f"Engine: {self.engine}\n"\
        f"Transmission: {self.trans}\n"\
        f"Drivetrain: {self.drivetrain}\n"\
        f"Doors: {self.doors}\n"\
        f"Color: {self.color}\n"
    
    def status(self):
        """Prints status of vehicle and accessories."""

        print(f"\nIgnition: {self.ign_status}\n"\
        f"Gear Selected: {self.gear_status}\n"\
        f"Drive Selected: {self.drive_status}\n"\
        f"Wipers: {self.wiper_status}\n"\
        f"Radio Station: {self.radio}\n"\
        f"Windows: {self.window_status}"\
        )
    
    def turn_ignition(self):
        """Lets user select ignition key position."""

        ign = input("1. Off, 2. ACC, 3. Run")   #Prints 3 option menu for user to select from.
        self.test_val = ign   #Variable used for test func
        if ign in ["1","2","3"]:
            if ign == "1":
                self.ign_status = "off"
                print("Ignition Off")
            elif ign == "2":
                self.ign_status = "acc"
                print("Ignition in accesory mode")
            else:
                self.ign_status = "run"
                print("Engine is running")
        else:
            print("Invalid Selection. Try again")   #Goes back to main menu if invalid input.
            self.test_val = [ign,"invalid"]

    
    def roll_window(self):
        """Function to allow user to roll windows up and down."""

        exit = False
        while exit == False:   #Loop runs until valid selection is made
            if self.ign_status == "run" or self.ign_status == "acc":   #Ignition key must be in run or accessorie mode to enable windows.
                window = input("1. Up\n2. Down\n")
                if window == "1":
                    self.window_status = "UP"
                    print("Windows Up")
                    exit = True
                elif window == "2":
                    self.window_status = "DOWN"
                    print("Windows Down")
                    exit = True
                else:
                    print("Invalid Selection")
                    continue
            else:
                print("Ignition is off")   #If ign is off exit to main menu so user can change key status.
                exit = True
        
    def wipers(self):
        """Lets user set wipers on or off"""

        exit = False   #Initialize exit variable for loop. Runs until valid selection is made
        if self.ign_status == "run" or self.ign_status == "acc":   #Wipers cannot be changed unless ign in run or accessory mode
            while exit == False:
                wiper = input("Wipers: Select ON/OFF ")   #Change class wiper status to what user selects
                if wiper in ["ON","on"]:
                    print("Wipers on... Squeek squeek")
                    self.wiper_status = wiper
                    exit = True
                elif wiper in ["OFF","off"]:
                    print("Wipers Off")
                    self.wiper_status = wiper
                    exit = True
                else:
                    print("Please type on or off")   #Loop if invalid input
                    continue
        else:
            print("Ignition is off")
    
    def adjust_radio(self):
        """Let user adjust radio setting"""

        exit = False
        while exit == False:
            freq = input("AM or FM: ")   #User selects AM or FM, loops until valid input made
            if freq in ["AM","FM"]:
                pass
            else:
                print("Invalid selection. Try again")
                continue

            self.radio = int(input("Enter a radio station between 87 and 108 (no decimals)"))   #No input validation because out of time

            if self.radio in range(87,108) and freq == "FM":   #Plays different stuff depending on if radio is in FM or AM mode
                print("*Music Plays*")
            elif self.radio in range(87,108) and freq == "AM":
                print("*Rush Limbaugh ranting sounds*")
            else:
                print("That station does not exist")   #Loops if invalid input
                continue
            exit = True

    def select_gear(self):
        """Allow user to select transmission gear"""

        exit = False
        while exit == False:
            if self.ign_status == "run":   #Gear cannot be changed unless vehicle is running
                gear = input("D = Drive\nR = Reverse\nP = Park\nN = Neutral\n")   #4 option menu for user to select from
                if gear in ["D","d"]:
                    self.gear_status = "D"
                    print(f"Vroom Vroom")
                    exit = True
                elif gear in ["R","r"]:
                    self.gear_status = "R"
                    print("Moving backwards beep beep!")
                    exit = True
                elif gear in ["p","P"]:
                    self.gear_status = "P"
                    print("Vehicle in Park")
                    exit = True
                elif gear in ["n","N"]:
                    self.gear_status = "N"
                    print("Vehicle in Neutral")
                    exit = True
                else:
                    print("Invalid selection")   #Loops back if invalid selection entered
                    continue
            else:
                print("Ignition is off")   #Exits to main menu if key position is invalid
                exit = True

    def select_drive(self):
        """Allow user to set 2wd or 4wd status."""
        exit = False
        while exit == False:
            if self.drivetrain == "2WD":   #If vehicle is not 4wd then selecting 4wd is not possible
                print("Your vehicle is 2 wheel drive, 4WD not available")
                exit = True
            elif self.drivetrain == "AWD":
                print("Your vehicle is all wheel drive at all times. 2WD not available")
                exit = True
            else:
                if self.ign_status == "run" and self.gear_status == "N":   #2wd/4wd status can only be changed if vehicle running and in neutral
                    drive = input("\n1. 2WD\n2. 4WD\n3. Return\n")   #2 option menu for user to select from
                    self.test_val = drive   #assign to test_val for test function use
                    if drive == "1":
                        self.drive_status = "2WD"
                        print("2WD Engaged")
                        exit = True
                    elif drive == "2":
                        self.drive_status = "4WD"
                        print("4WD Engaged")
                        exit = True
                    elif drive =="3":
                        exit = True
                    else:
                        print("Invalid Selection")
                        continue
                elif self.ign_status == "run" and self.gear_status != "N":   #If vehicle running but not in neutral print and exit to main menu
                    print("Vehicle must be in neutral to change into 2WD/4WD")
                    exit = True
                else:   #Exit to main menu if vehicle not runnning
                    print("Ignition must be in Run position")
                    exit = True

def select_drive_test():
    """Test function for select_drive method of class type Car."""
    test_car = Car()
    test_car.ign_status = "run"   #Enable all variables required by select_drive to be able to change drive status
    test_car.gear_status = "N"
    test_car.drivetrain = "4WD"
    test_car.select_drive()
    if test_car.test_val == "1" and test_car.drive_status == "2WD":
        print("pass")
    elif test_car.test_val == "2" and test_car.drive_status == "4WD":
        print("pass")
    elif test_car.test_val == "3" and test_car.drive_status == "2WD":   #2wd is default value for car.drive_status, option 3 makes no changes
        print("pass")
    else:
        print("fail")

def ign_change_test():
    """Test function for ign key method in Car class"""
    test_car = Car()
    test_car.turn_ignition()
    if test_car.test_val == "1" and test_car.ign_status == "off":
        print("Pass")
    elif test_car.test_val == "2" and test_car.ign_status == "acc":
        print("Pass")
    elif test_car.test_val == "3" and test_car.ign_status == "run":
        print("Pass")
    elif test_car.test_val[0] not in ["1","2","3"] and test_car.test_val[1] == "invalid":
        print("Pass")
    else:
        print("Fail")

def main():
    my_car = Car()

    exit_menu = False   #Initialize loop exit variable
    while exit_menu == False:
        
        user = input("\nType 0 to Quit\n"   #7 option user menu
            "1. Choose your car\n"   #Lets user choose all of their vehicle optons
            "2. Turn key\n"   #Change ign key status
            "3. Accessories\n"   #Enter accessory menu
            "4. Select Gear\n"   #Select transmission gear
            "5. Select 2WD/4WD\n"   
            "6. View Vehicle Status\n"   #Shows vehicle accessories status
            "7. View Vehicle Info\n"   #Shows current vehicle information
            )

        if user in ["1","2","3","4","5","6","7"]:   #Loops back to main menu if invalid entry
            pass
        elif user == "0":
            exit_menu = True
        else:
            print("Invalid Selection")
            continue

        if user == "1":   #User enters all vehicle information
            my_car.make = input("Enter make: ")
            my_car.model = input("Enter model: ")

            engine_selection = input("Enter engine type:\n1.4 Cyl\n2.V6\n3.V8\n4.V12\n")   #Only allow certain engine types
            if engine_selection in ["1","2","3","4"]:   #loop back to main menu if invalid input. This could be done better, but time
                if engine_selection == "1":
                    my_car.engine = "4cyl"
                elif engine_selection == "2":
                    my_car.engine = "v6"
                elif engine_selection == "3":
                    my_car.engine = "v8"
                else:
                    my_car.engine = "v12"
            else:
                print("Invalid Selection. Returning ")
                continue
            
            color_list = ["Secret","Black","Red","Blue","White","Green"]   #List of colors to ref menu slection to
            color = input("Choose a color:\n1.Black\n2.Red\n3.Blue\n4.White\n5.Green\n")   #5 option menu
            if color in ["0","1","2","3","4","5"]:
                color = int(color)   #Change user input to an integer type for list indexing
                my_car.color = color_list[color]   #Change car color to chosen color in color list
            else:
                print("Invalid Selection")
                continue

            drivetrain_selection = input("Enter Drivetrain Type:\n1. 2WD\n2. 4wd\n3. AWD\n")   #Allow only 3 drivetrain options to choose from
            if drivetrain_selection == "1":
                my_car.drivetrain = "2WD"
                print(my_car)   #Prints entire vehicle info once all options have been selected
                continue
            elif drivetrain_selection == "2":
                my_car.drivetrain = "4WD"
                print(my_car)
                continue
            elif drivetrain_selection == "3":
                my_car.drivetrain = "AWD"
                print(my_car)
                continue
            else:
                print("Invalid Selection")
                continue

        if user == "2":   #Menu selection suite
            my_car.turn_ignition()
        elif user == "3":
            acc = input("1. Radio\n2. Wipers\n3. Windows\n")   #Choose accessory to be modified
            if acc in ["1","2","3"]:
                if acc == "1":
                    my_car.adjust_radio()
                elif acc == "2":
                    my_car.wipers()
                else:
                    my_car.roll_window()
            else:
                print("Inavlid Input")
        elif user == "4":
            my_car.select_gear()
        elif user == "5":
            my_car.select_drive()
        elif user == "6":
            my_car.status()
        else:
            print(my_car)

if __name__ == "__main__":
    main()





