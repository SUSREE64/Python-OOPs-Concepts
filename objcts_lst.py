# In this example we can see the a class for a pair of numbers
# various methods to work on those numbers
# while instantiating, without using a variable name how we can still access a method from an instance
# keeping the objects instances in an array


class NumPair:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiply(self):
        return (self.num1*self.num2)
    def add(self):
        return(self.num1+self.num2)
    def max(self):
        return (max(self.num1, self.num2))
    def min(self):
        return(min(self.num1,self.num2))
#objects list
obj_arr = []
#number pairs as tuples in a list
pairs = [(20,2), (30,2), (12, 15)]
# creating the objects and pushing them to an array
for i in pairs:
    obj_arr.append(NumPair(i[0], i[1]))
print("The numbers: {} , {}, and result of multiply ,{}".format(obj_arr[0].num1, obj_arr[0].num2, obj_arr[0].multiply()))
print("The numbers: {} , {}, and result of add ,{}".format(obj_arr[0].num1, obj_arr[0].num2, obj_arr[0].add()))
print("The numbers: {} , {}, and result of min ,{}".format(obj_arr[2].num1, obj_arr[2].num2, obj_arr[2].min()))
#Instantiating and running the method on the fly.
print(NumPair(30,2).multiply())
