class Vehicle:
    
    def __init__(self, name, model, milage ):
        self.name = name
        self.model = model
        self.milage = milage
        
    def show_details(self):
        print("Vehicle name :", self.name)
        print("Vehicle Model:", self.model)
        print("Vehicle Milage:", self.milage)
        
#declare a child call for Vehicle
#by mentioning Vechile in brackets Bus becomes the child class of Vehicle
#all the methods, variables of Vehicle get in herited by Bus class
class Bus(Vehicle):
    pass

obj1 = Bus("School Bus", "Ashok Leyland", 25)

obj1.show_details() 
