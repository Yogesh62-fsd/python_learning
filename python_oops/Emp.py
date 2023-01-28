class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print(f'name is {self.name} age is {self.age} salary is {self.salary} ')
    def show(self):
        print(f'name is {self.name} age is {self.age} salary is {self.salary} department is {self.department}')

e1=Emp('ashish',20,30000)
print(e1)
print(type(e1))
e1.display()

# Another way of adding the  instance variable to object
# by using the __dict__()
# it is special instance variable managed by pyhon for every object which stores the all the attributes of object in
# key value pair form

print(e1.__dict__) #{'name': 'ashish', 'age': 20, 'salary': 30000}

# we can also add new attribute to the object using this __dict__

e1.__dict__['department']='Human Resource'
e1.show()
print(e1.__dict__)

# we can also change the value of any adttribute using the __dict__
e1.__dict__['name']='Yogesh'
print(e1.__dict__)

print(e1.__dict__['department'])
print(e1.__dict__.get('name'))


