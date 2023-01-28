class Emp:
    def __init__(self,name,age,salary,department,profile):
        self.name=name
        self.age=age
        self.salary=salary
        self.department=department
        self.profile=profile
    def display(self):
        print(f'name is {self.name} age is {self.age} salary is {self.salary} Department is {self.department}')

    def show_details(self):
        print(f'name is {self.name} age is {self.age} salary is {self.salary} Profile is {self.profile}')

    def remove_attribute(self):
        del self.profile
# now we can also delete any attribute in python
# n=by using del operator

e=Emp('yogesh','22',34000,'It','Softwareengg.')
e.display()


del e.department
# print(e.display())  #after deleting if call the display then it will give Attribute Error

print(e.show_details())

# now deleting the attribute profile using  the any class method
e.remove_attribute()
# print(e.show_details()) this will give  Attribute Error