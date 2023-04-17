class Employee:
    def getter(self):
        Employee.name = input("Enter name: ")
        Employee.ID = int(input("Enter ID: "))
        Employee.sal = int(input("Enter salary: "))
    def display(self):
        print("The details of employee are: ")
        print("ID:",Employee.ID)
        print("Name:",Employee.name)
        print("Salary:",Employee.sal)
        print("HRA:",self.HRA())
        print("DA:",self.DA())
        print("Gross Salary:",self.Gross())
        print("Net Salary:",self.Net())
    def HRA(self):
        return (0.18*(Employee.sal))
    def DA(self):
        return (0.1*(Employee.sal))
    def Gross(self):
        return ((Employee.sal)+self.HRA()+self.DA())
    def Net(self):
        return (0.9*self.Gross())

emp = Employee()
emp.getter()
emp.display()
