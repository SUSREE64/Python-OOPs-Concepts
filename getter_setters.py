"""getter and setters are methods to get values or set value of 
instance variables of a class. Often the logic associated with input validation
is used while setting the value of an attribute. Setter method gives advantage of 
updating the value with correct type of data thus protects the data elements 
"""
class Car:
    
    def __init__(self, manufacturer, model, year, price):
        self._manufacturer = manufacturer
        self._model = model
        self._year = year
        self._price = price
    # getter methods to return the values of the attributes.   
    def get_manufacturer(self):
        return self._manufacturer
    def get_model(self):
        return self._model
    def get_year(self):
        return self._year
    def get_price(self):
        return self._price
    #setter methods to set the value of the attributes
    def set_manufacturer(self, new_manufacturer):
        if isinstance(new_manufacturer, str):
            self._manufacturer = new_manufacturer
        else:
            print("please enter a string for Manufacturer")
   
#Create an objct of the Car class.   
vehicle = Car("Maruthi", "Alto", 2000, 3.5)

print(vehicle.get_manufacturer())

vehicle.set_manufacturer(1234) #gives input validation warning. 
print(vehicle.get_manufacturer())

vehicle.set_manufacturer("Nisson") #Accepts the Nisson value 
print(vehicle.get_manufacturer())
