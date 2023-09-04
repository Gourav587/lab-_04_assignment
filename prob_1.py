## Assignment: 1
class Employee:
    def __init__(self,Id,name,age,salary):
        self.Id=Id
        self.name=name
        self.age=age
        self.salary=salary
        
  
    def __repr__(self):
        return f"Employee ID: {self.Id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


def sort_employee_data(employees, sorting_parameter):
    if sorting_parameter == 1: 
        return sorted(employees, key=lambda emp: emp.age)
    elif sorting_parameter == 2: 
        return sorted(employees, key=lambda emp: emp.name)
    elif sorting_parameter == 3: 
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")


employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]
sorting_parameter = int(input("Enter the sorting parameter (1. Age, 2. Name, 3. Salary): "))
sorted_employees = sort_employee_data(employees, sorting_parameter)
for employee in sorted_employees:
    print(employee)