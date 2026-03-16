class Student:
    def __init__(self, name: str, gpa: float, major: str) -> None:
        self.name = name
        self.gpa = gpa
        self.major = major

    def is_on_honor_roll(self) -> bool:
        return self.gpa > 3.5


if __name__ == "__main__":
    # Create a sample Student object
    student = Student("Alice Johnson", 3.8, "Computer Science")

    # Test the honor roll method
    result = student.is_on_honor_roll()

    # Print the result
    print(f"Student: {student.name}")
    print(f"GPA: {student.gpa}")
    print(f"Major: {student.major}")
    print(f"On Honor Roll: {result}")