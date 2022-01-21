class A:
    # Constructor    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def product(self):
        return (self.x*self.y )  

class B(A): # Child class of Parent A or Subclass of A.
    #Constructor 
    # with this , the arguments passed while creating the instance can be passed to super/parent class
    def __init__(self, *args):
        super(B, self).__init__(*args)
    
    # Child has its own method
    def sum_up(self):
        return (self.x+self.y)
    


a1 = A(20,30)
b1 = B(2,3)
#b1 = B(30, 40)
# b1 object is a instance of class b
# b1 can use the method of A to get the product of the numbers
print(f" The sum of {b1.x} and {b1.y} is {b1.sum_up()}") 
print (f" The product of {b1.x} and {b1.y} is {b1.product()}")      
