


'''
In this mini project, a music School hired me to add functionality to an existing program that is used
to keep a centralized record of all their students across their headquarters

My job is to add three methods to the existing program:
1) Should be a method <print_statement_data> that prints the name of each one of the students
in the dictionary, their age, and the classes they are taking, one student per line

2) The second method <print_student> prints the string showing the name, age, and classes of a student.
it should take the name of the student as an argument and print only the data of that particular student.

3) The second method should be <add_student> that adds a student to the existing <students> dictionary.
The key used to add the student to the dictionary should be the name of the student and the value should be
a list with the age, phone number, and classes that the student is taking.
The method will take the name of the student as a parameter and a list with the data associated with that name
as another parameter.


'''

########## Algorithm #########
### create a class MusicSchool
###  create a dictionary of class attribute name students: containing the names of the students as keys
######## and the list of their data as values
### create a constructor for the class with parameters working_hours and revenue
#### the constructor has instance attributes working_hours and revenue

#### Build the methods of the class:
###     define a method called-  print_students_data----parameter---> self since it inherits a method print_student
###     define a second method- print_student---with arguemnt----> name and follows steps in doctring 2
###      define a methos- add_student that adds a student to the existing students dictionary--- follow doctring3

###

class MusicSchool:

    students = {'Gino':     [15, '653-235-345', ['Piano, Guitar']],
                'Talina':   [28, '555-765-452', ['Cello']],
                'Eric':     [12, '583-356-223', ['singing']]
                }

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
        self.no_students = []


    #greating the first method
    def print_student_data(self):
        for name in MusicSchool.students: ## this print the data of all the student by using the method below
            self.print_student(name)

   ## this method is created to have its used in the code above
    def print_student(self, name): ## But the method prints the student data, student by student
        data = MusicSchool.students[name]
        print('Student:' + name + ' who is ' + str(data[0]) + ' and is taking ' + str(data[2]) )

    def add_student(self, name, data):
        MusicSchool.students[name] = data

    ## i want to create method to remove people from the dictionary
    def remove_student(self, name):
        if name in MusicSchool.students:







headquarter1 = MusicSchool(8, 15000)

#headquarter1.print_student_data()
headquarter1.add_student('Daniel', [24, '08066610922', ['Violin']])

#headquarter1.print_student_data()
headquarter1.remove_student('Daniel')
headquarter1.print_student_data()

