class A:
    # Constructor    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def product(self):
        return (self.x*self.y )  
    def exponent(self):
        return (self.x**self.y)    

class B(A): # Child class of Parent A or Subclass of A.
    #Constructor 
    # with this , the arguments passed while creating the instance can be passed to super/parent class
    def __init__(self, *args):
        super(B, self).__init__(*args)
    
    # Child has its own method
    def sum_up(self):
        return (self.x+self.y)
    


a1 = A(5,2)
b1 = B(2,3)
# b1 object is a instance of class b. It can access its own methods, and methods of A 
# b1 can use the method of A to get the product of the numbers
print(f" The sum of {b1.x} and {b1.y} is {b1.sum_up()}") 
print (f" The product of {b1.x} and {b1.y} is {b1.product()}") 
print(f"{a1.x} to the power of  {a1.y} is {a1.exponent()}")
print(f"{b1.x} to the power of {b1.y} is {b1.exponent()}")     
