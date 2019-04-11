
class Employee:
  '''Common base class for all employees'''
  empCount = 0
  

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1 #you can use the class data inside the classes methods

  def displayCount(self):
    print ("Total Employee {0}" .format(Employee.empCount))

  def displayEmployee(self):
    print ("Name : {0:<10} Salary: {1:<5}".format(self.name,self.salary))

#create the instances
'''This would create first object of Employee class'''
emp1 = Employee("Doug", 5000)
'''This would second first object of Employee class'''
emp2 = Employee("Nemo", 2000)

#accessing the attributes
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee {0}".format( Employee.empCount))
