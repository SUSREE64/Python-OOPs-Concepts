class Fruit:
    
    def __init__(self, name, color, taste):
        self._name = name
        self._color = color
        self._taste = taste
        
    #getter methods    
    def get_name(self):
        return self._name
    def get_color(self):
        return self._color
    def get_taste(self):
        return self._taste
    
    #setter methods
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Please give a valid string for name")
    
    def set_color(self, new_color):
        if isinstance(new_color, str):
            self._color = new_color
        else:
            print("Please give a valid string for name")
    def set_taste(self, new_taste):
        if isinstance(new_taste, str):
            self._taste = new_taste
        else:
            print("Please give a valid string for name")
    #Please note that first getter has to be there followed by setter.
    name = property(get_name, set_name)
    color = property(get_color, set_color)
    taste = property(get_taste, set_taste)

#########################################
#outside class #####
mango = Fruit("Mango", "Yellow", "Sweet");

print(mango.get_name())
mango.set_name("Benishan")
print(mango.get_name())
print(mango.name)
mango.color = "saffron"
print(mango.color)
