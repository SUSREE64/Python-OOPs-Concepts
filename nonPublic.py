""" 
In Python, there are no Public, Private keywords and there are no 
access modifiers . There are public, and non-public attributes only
there are no private attributes. Every attribute is accesable but
by a special naming convension of adding _underscore before the attribute
we indicate that the attribute is not supposed to be accessed from outside of 
class"""

class Student:
    
    _college = "venkateswara"
    __university = 'Trinity'
    
    def __init__(self, name, age, gpa, town):
        self.name = name
        self._age = age # by adding an leading underscore making this non-public
        self.gpa = gpa
        self.__town = town ## by adding two leading underscores, making this completely not accessible
        
    def show_college(self):
        print(self._college)
        
std1 = Student('Raj', 32, 3.89, 'Kurnool')

print(std1.name) ## This is OK
#print(std1.age) ## this is not OK gives error
print(std1._age) ## this is possible -        

#print(std1.town) ## This is not Ok
#print(std1.__town) ## This also is not OK

#print(Student.college) ##This is not OK
print(Student._college) # this is posslble
std1.show_college() 
#print(Student.university) #This is not possible
#print(Student.__university) #This is not possible
#print(Student._university) #This is not possible

