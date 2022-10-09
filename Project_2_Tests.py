from Project_2_beta import Car

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

select_drive_test()
ign_change_test()