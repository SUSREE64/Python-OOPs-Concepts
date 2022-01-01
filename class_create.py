"""
Class :  The class is a user defined data structure that binds data, methods into a single unit.
Class is a blue print or code template for objects creation
In the below example, class Book is created with obj_name, title, author, category, year_published 
these are all instance variables. 
def __init__ initialization function while object is created.
Object : The object is an instance of Class. Multiple objects can be created from a Class template
In the below example two instances b1, b2 are created for Book Class
"""
#class creation
class Book:
    #initialization function and instance variables
    def __init__ (self, obj_name, title, author, category, year_published):
        self.obj_name = obj_name
        self.title = title
        self.author = author
        self.category = category
        self.year_published = year_published
        print("The book object {} is created".format(self.obj_name))

   # Class Method
    def show_details(self):
        print( "The details of object", self.obj_name)
        print("********************************")
        print ("Title :", self.title)
        print("Author :", self.author)
        print("Category:", self.category)
        print("Year Published:", self.year_published)
#Creating instances of the class
b1 = Book("b1","Gods must be crazy", "Robert", "Fiction", 1962)
b2 = Book("b2", "Good to great", "Jim Collins", "Business", 1964)

b1.show_details()
b2.show_details()
