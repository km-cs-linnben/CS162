class Course:
    """Teacher, subject, name, grade."""
    def __init__(self, course_num=0, subject="", course_name="", crn="", credits=0, delivery_mode="", instructor=""):
        # convention for "private" attributes. Prefix: one underscore; two two underscores.
        self._course_num = course_num
        self._subject = subject
        self._course_name = course_name
        self._crn = crn
        self._credits = credits
        self._delivery_mode = delivery_mode
        self._instructor = instructor
    
    def __str__(self):
        return f"{self._course_num} {self._subject} {self._course_name} {self._crn}" \
               f"{self._credits} {self._delivery_mode} {self._instructor}"

    # set methods to set the values of each attributes
    def set_course_num(self, num):
        self._course_num = num
    def set_subject(self, subject):
        self._subject = subject
    def set_course_name(self, course_name):
        self._course_name = course_name
    def set_crn(self, crn):
        self._crn = crn
    def set_credits(self, credits):
        self._credits = credits
    def set_delivery_mode(self, delivery_mode):
        self._delivery_mode = delivery_mode
    def set_instructor(self, instructor):
        self._instructor = instructor

    def get_course_num(self):
        return self._course_num
    def get_subject(self):
        return self._subject
    def get_course_name(self):
        return self._course_name
    def get_crn(self):
        return self._crn
    def get_credits(self):
        return self._credits
    def get_delivery_mode(self):
        return self._delivery_mode
    def get_instructor(self):
        return self._instructor

course_1 = Course(
    course_num=160, 
    subject="CS",
    course_name="Intro to CS",
    crn = "50978",
    credits = 4,
    delivery_mode = "Virtual",
    instructor="Baby Wang"
    )

course_2 = Course(
    course_num=211, 
    subject="WR",
    course_name="Creative Writing",
    crn = "23798",
    credits = 4,
    delivery_mode = "Virtual",
    instructor="Simons"
    )


class TermSchedule:
    """Student, course list"""
    def __init__(self, courses=[]):
        self._courses = courses # a list of Course objects

    def add_course(self, course):
        """Add course object."""
        self._courses.append(course)
    
    def print_schedule(self):
        """Print out current schedule."""
        for course in self._courses:
            print(course)

schedule = TermSchedule()
schedule.print_schedule()
# maybe use pretty table
schedule.add_course(course_1)
schedule.add_course(course_2)
schedule.print_schedule()