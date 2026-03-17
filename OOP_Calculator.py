class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        return a / b


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Invalid input! Please enter a numeric value.")


def get_operation() -> str:
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in valid_operations:
            return op
        print("⚠️ Invalid operation! Please choose from +, -, *, /.")


def perform_calculation():
    calc = Calculator()
    while True:
        try:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            operation = get_operation()

            if operation == '+':
                result = calc.add(num1, num2)
            elif operation == '-':
                result = calc.subtract(num1, num2)
            elif operation == '*':
                result = calc.multiply(num1, num2)
            elif operation == '/':
                try:
                    result = calc.divide(num1, num2)
                except ZeroDivisionError:
                    print("⚠️ Error: Cannot divide by zero!")
                    continue

            print(f"Result: {result}")

        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")

        finally:
            cont = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if cont != 'y':
                print("✅ Thank you for using the calculator. Goodbye!")
                break


if __name__ == '__main__':
    perform_calculation()