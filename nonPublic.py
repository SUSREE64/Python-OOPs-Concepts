""" 
In Python, there are no Public, Private keywords and there are no 
access modifiers . There are public, and non-public attributes only
there are no private attributes. Every attribute is accesable but
by a special naming convension of adding _underscore before the attribute
we indicate that the attribute is not supposed to be accessed from outside of 
class"""

class Student:
    
    _college = "venkateswara"
    
    def __init__(self, name, age, gpa):
        self.name = name
        self._age = age # by adding an leading underscore making this non-public
        self.gpa = gpa
        
    def show_college(self):
        print(self._college)
        
std1 = Student('Raj', 32, 3.89)

print(std1.name) ## This is OK
#print(std1.age) ## this is not OK gives error
print(std1._age) ## this is possible -        

#print(Student.college) ##This is not OK

std1.show_college()
