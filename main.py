#1-m
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if 0 < new_salary:
            self.__salary = new_salary
        else:
            print("Salary can't be less than zero")
            
            
e1 = Employee("John", 20000)

print(e1.name)
print(e1.get_salary())

e1.set_salary(8)
print(e1.get_salary())

e1.set_salary(9)
print(e1.get_salary())
