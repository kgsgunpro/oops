#iniating a class 
class Employee:
    # constructor
    def __init__(self):
        print('started executing attributes/data')
        self.id =123
        self.salary= 40000
        self.designation = 'sde'
        print('started executing attributes/data')
# creating obj/instance of class
    def travel(self,destination):
        print('travel func called manually')
        print(f'employee is now traveling to { destination}')
ravi = Employee()
print(ravi.salary , ravi.travel('vizag'))
print(type(ravi))

