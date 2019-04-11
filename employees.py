
class Employee:

  # create the class variables
  raise_amount=1.04
  employee_amount=0

  # initialise the class attributes
  def __init__(self, first, last, pay):
    
    self.first=first
    self.last=last
    self.pay=pay
    self.email=first+last+'@company.com'
    
    Employee.employee_amount+=1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def Raise(self):
    self.pay=int(self.pay*self.raise_amount)
    print(self.pay)

class Developer(Employee):
  raise_amount=1.10

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    #Employee.__init__(self, first, last, pay)
    self.prog_lang=prog_lang

class Manager(Employee):
  raise_amount=5.50
  def __init__(self,first,last,pay,employees=None):
    super().__init__(first,last,pay)
    if employees is None:
      self.employees=[]
    else:
      self.employees=employees

  def add_employee(self, fullname):
    self.employees.append(fullname)

  def remove_employee(self, fullname):
    self.employees.remove(fullname)

  def print_employees(self):
    for each in self.employees:
      print(each.fullname())

emp_1=Employee('Bob','Smith',50000)
emp_2=Employee('Gary','Davis',60000)

dev_1=Developer('Julie','Michaels',50000, 'php')
dev_2=Developer('Chris','Lewis',60000, 'Python')

mgr_2=Manager('Stephen', 'Johnson', 80000,[dev_1])
mgr_1=Manager('Maria', 'Turner', 80000)

mgr_2.Raise()
dev_1.Raise()
dev_2.Raise()

print(emp_2.email)

print(Employee.employee_amount)

mgr_2.print_employees()

