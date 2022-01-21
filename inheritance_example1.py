"""
The Inheritance OOP Concept explined below

"""

class A:
    
    def feature_of_a_1(self):
        print("The method of Class A is invoked here");
    
    
class B(A): # By adding the A inside the brackets of A, we are giving inheretance

    def feature_of_b_1(self):
        print("The method of Class B  is invoked here");

class C:
    def feature_of_c_1(self):
        print("The method of Class C  is invoked here");

# Intances of above three classes are created
a1 = A()
b1 = B()
c1 = C()  

# What all can be Accessed. 
a1.feature_of_a_1()
# b1 is inheriting the Class A hence we can access Calss A Methods also 
b1.feature_of_a_1()
b1.feature_of_b_1()
