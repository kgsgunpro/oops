#iniating a class 
class Employee:
    # constructor
    def __init__(self):
        self.id =123
        self.salary= 40000
        self.designation = 'sde'
# creating obj/instance of class
    def travel(self,destination):
        print(f'employee is now traveling to { destination}')
ravi = Employee()
print(ravi.salary , ravi.travel('vizag'))

