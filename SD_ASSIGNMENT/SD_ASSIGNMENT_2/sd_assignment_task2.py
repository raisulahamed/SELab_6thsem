class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15

# Demonstrating Polymorphism
employees = [
    Manager("Amjad", "C223085", 80000),
    Developer("Raisul", "C223114", 60000),
    Employee("Sadi", "C223118", 50000)
]

for emp in employees:
    print(f"{emp.name} (ID: {emp.emp_id}) Bonus: ${emp.calculate_bonus():.2f}")