class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def __str__(self):
        return f"Employee: {self.name}, ID: {self.emp_id}, Salary: ${self.salary:.2f}"

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20  # Manager gets 20% bonus

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15

def show_bonus(employee):
    print(f"{employee.name}'s Bonus: ${employee.calculate_bonus():.2f}")

emp1 = Employee("Alice", 101, 50000)
emp2 = Manager("Bob", 102, 70000)
emp3 = Developer("Charlie", 103, 60000)

show_bonus(emp1)
show_bonus(emp2)
show_bonus(emp3)
