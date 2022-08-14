""" In this snippet, class attributes are used. 
class attributes are variable that are accessible with self. notation and are common to all the instances.""" 



class Employee:
    #class attributes
     hra_fact = 0.5
     spl_fact = 0.5
     pf_fact =  0.12
     
     def __init__(self, name, age, title, basic):
        #instance attributes
        self.name = name
        self.age = age
        self.basic = basic
        self.hra = self.hra_fact*basic
        self.spl = self.spl_fact*basic
        self.pf = self.pf_fact*basic
        
     def printsalary(self):
         print("Name :", self.name)
         print("Basic:", self.basic)
         print("H.R.A:", self.hra)
         print("Special Allowance :", self.spl)
         print("Provident Fund :", self.pf)
         print("Total Salary :", self.basic+self.hra+self.spl+self.pf)
         
         
emp1 = Employee(name = "Raju", age = 52, title = "Sr Asst", basic = 22500)

emp1.printsalary()
#class attribute is accissible
print(emp1.pf_fact) # from the instance
print(Employee.pf_fact) #from the class
