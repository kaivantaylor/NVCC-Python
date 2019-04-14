# PURPOSE: Demonstrate inheritance in Python.
# CSC 201 - Computer Science I
# Name: Kaivan Taylor

#---------------------class Person-----------------------------#

class Person(object):
    def __init__(self, first_name = '', last_name = ''):
        '''Create a person: first name, last name. Defaults
           are null strings.'''
        self.__last_name = last_name
        self.__first_name = first_name

    def __str__(self):
        result_str = "Name: {}".format( self.__last_name + ", " + \
                                        self.__first_name)
        return result_str

#--------------------Person Methods---------------------------#

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

#------------------------class Student------------------------#

class Student(Person):
    
    def __init__(self, first_name = '', last_name = '', student_id = 0, \
                 residency = 'Out-of-state'):
        '''Create a student: first name, last name, student id, residency(y/n).'''
        Person.__init__(self, first_name, last_name)
        self._student_id_number = student_id
        if residency == 'In-state':
            self._student_residency = "In-state"
        else:
            self._student_residency = residency

    def __str__(self):
        result_str = Person.__str__(self)
        result_str = result_str + " ; Student id: {}, Residency: {}".format\
                     (self._student_id_number, self._student_residency)
        return result_str

#----------------------Class Methods--------------------------#

    def get_student_id(self):
        return self._student_id_number

    def get_residence_status(self):
        return self._student_residency

    def set_student_id(self, new_student_id):
        self._student_id_number = new_student_id

    def set_resident_status(self, new_resident):
        self._student_residency = new_resident

#--------------------class Undergrad--------------------------#

class Undergrad(Student):

    def __init__(self, first_name = '', last_name = '', student_id = 0, \
                 residency = 'Out-of-state', class_number = 1, gpa = 4.0,\
                 graduate_status = 'Not Graduated'):
        '''Create an undergrad: first name, last name, class number, gpa, graduate status.'''
        Student.__init__(self, first_name, last_name, student_id, residency)
        
        if 4 >= class_number >= 1: # Instance made for Undergrad class number.
            self._undergrad_class_number = class_number
        else:
            self._undergrad_class_number = "1"

        if 4 >= gpa >= 0: # Instance made for Undergrad gpa.
            self._undergrad_gpa = gpa
        else:
            self._undergrad_gpa = "4.0"

        self._graduate_status = graduate_status # Instance made for Undergrad graduate status.

    def __str__(self):
        result_str = Student.__str__(self)
        result_str = result_str + " ; Class number: {}, GPA: {}, Graduate Status: {}".format\
                     (self._undergrad_class_number, self._undergrad_gpa, self._graduate_status)
        return result_str

#-----------------------------Undergrad Methods----------------------------#
    
    def get_undergrad_class_number(self):
        if self._undergrad_class_number == 1:
            return (self._undergrad_class_number, "Freshman")
        elif self._undergrad_class_number == 2:
            return (self._undergrad_class_number, "Sophomore")
        elif self._undergrad_class_number == 3:
            return (self._undergrad_class_number, "Junior")
        elif self._undergrad_class_number == 4:
            return (self._undergrad_class_number, "Senior")
        else:
            self._undergrad_class_number = 5
            return ("N/A")
    def get_undergrad_gpa(self):
        return self._undergrad_gpa
    
    def get_undergrad_status(self):
        return self._graduate_status

    def complete_undergrad_year(self):
        if self._undergrad_class_number == 4:
            self._graduate_status = "Graduated"
            self._undergrad_class_number = self._undergrad_class_number + 1
            print("Congratulations! You Graduated!")
        else:
            self._undergrad_class_number = self._undergrad_class_number + 1
            print("Completed one year!")
            
    def set_undergrad_gpa(self, gpa):
        if 4 >= gpa >= 0:
            self._undergrad_gpa = gpa
        else:
            print("Invalid GPA!")

    def set_undergrad_class_number(self, number):
        if 4 >= number >= 1:
            self._undergrad_class_number = number
        elif number == 5:
            print("You graduated!")
            self._undergrad_class_number = 5
        else:
            print("Invalid number!")

    def set_undergrad_status(self, status):
        self._graduate_status = status

#-----------------------------TEST USING ASSERT---------------------------------#
p1 = Person("Kaivan","Taylor")
assert p1.get_first_name() == 'Kaivan' # Verifying current first name
assert p1.get_last_name() == 'Taylor' # Verifying current last name

p1.set_first_name("Test1") # Setting first name, then verifying
assert p1.get_first_name() == 'Test1'

p1.set_last_name("Test2") # Setting last name, then verifying
assert p1.get_last_name() == 'Test2'

#**************************** TEST FOR PERSON CLASS ************************#

s1 = Student("Rick", "Sanchez", "321", "Out-of-state")

assert s1.get_first_name() == 'Rick' # Verifying current first name
assert s1.get_last_name() == 'Sanchez' # Verifying current last name

s1.set_first_name("Test3") # Setting first name, then verifying
assert s1.get_first_name() == 'Test3'

s1.set_last_name("Test4") # Setting last name, then verifying
assert s1.get_last_name() == 'Test4'

assert s1.get_residence_status() == 'Out-of-state' # Verifying current residency.

s1.set_resident_status("In-state") # Setting residency, then verifying
assert s1.get_residence_status() == 'In-state'

assert s1.get_student_id() == "321" # Verifying current student id

s1.set_student_id("777") # Setting student id, then verifying
assert s1.get_student_id() == "777"

#*************************TEST FOR UNDERGARD CLASS****************************#

u1 = Undergrad("Timothy", "Seaman", "999", "In-state", 3, 4.0, "Graduated")

assert u1.get_first_name() == 'Timothy' # First name
assert u1.get_last_name() == 'Seaman' # Last name

u1.set_first_name("Test5") # Setting first name then verifying
assert u1.get_first_name() == 'Test5' 

u1.set_last_name("Test6") # Setting last name then verifying
assert u1.get_last_name() == 'Test6'

assert u1.get_residence_status() == 'In-state' # Verifying current residency

u1.set_resident_status("Out-of-state") # Setting residency, then verifying
assert u1.get_residence_status() == 'Out-of-state'

assert u1.get_student_id() == "999" # Verifiying student id

u1.set_student_id("194") # Setting student id, then verifying
assert u1.get_student_id() == "194"

assert u1.get_undergrad_class_number() == (3, 'Junior') # Verifying current class

u1.set_undergrad_class_number(1) # Setting class, then verifying
assert u1.get_undergrad_class_number() == (1, 'Freshman')

assert u1.get_undergrad_gpa() == 4.0 # Verifying current gpa

u1.set_undergrad_gpa(3.5) # Setting gpa, then verifying
assert u1.get_undergrad_gpa() == 3.5

assert u1.get_undergrad_status() == "Graduated" # Verifying current grad status

u1.set_undergrad_status("Not Graduated") # Setting grad status, then verifying
assert u1.get_undergrad_status() == "Not Graduated"

print("END OF ASSERT TEST - NO ERRORS")



