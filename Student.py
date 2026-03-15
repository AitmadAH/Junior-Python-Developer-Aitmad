class Student:
    def __init__(self, name: str, gpa: float, major: str) -> None:
        self.name = name
        self.gpa = gpa
        self.major = major

    def display_info(self) -> None:
        print(f"Name : {self.name}")
        print(f"GPA  : {self.gpa}")
        print(f"Major: {self.major}")
        print("-" * 30)


if __name__ == "__main__":
    # Create example Student objects
    student_1 = Student("Alice Johnson", 3.8, "Computer Science")
    student_2 = Student("David Smith", 3.5, "Data Science")

    # Display their attributes
    print("Student Information")
    student_1.display_info()
    student_2.display_info()