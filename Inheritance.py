class Employee:
    def __init__(self, name: str, employee_id: int, salary: float):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}"


class Developer(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, programming_language: str):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):

        base_info = super().display_info()
        return f"{base_info}, Programming Language: {self.programming_language}"


class Manager(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, team_size: int):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Team Size: {self.team_size}"


if __name__ == '__main__':
    # Instantiate a Developer and a Manager
    dev = Developer(name="Alice", employee_id=101, salary=75000, programming_language="Python")
    mgr = Manager(name="Bob", employee_id=102, salary=90000, team_size=5)

    # Print their information
    print(dev.display_info())
    print(mgr.display_info())