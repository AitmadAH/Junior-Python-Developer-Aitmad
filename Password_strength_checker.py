import re
import sys
import unittest
from typing import List, Tuple


class PasswordStrengthChecker:

    MIN_LENGTH = 8

    def evaluate_password(self, password: str) -> Tuple[str, List[str]]:

        score = 0
        suggestions = []

        if len(password) >= self.MIN_LENGTH:
            score += 1
        else:
            suggestions.append("Increase password length to at least 8 characters.")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            suggestions.append("Add at least one uppercase letter.")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            suggestions.append("Add at least one lowercase letter.")

        if re.search(r"\d", password):
            score += 1
        else:
            suggestions.append("Include at least one number.")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            suggestions.append("Add at least one special character.")

        strength = self._determine_strength(score)

        return strength, suggestions

    @staticmethod
    def _determine_strength(score: int) -> str:

        if score <= 2:
            return "Weak"
        if score <= 4:
            return "Medium"
        return "Strong"


def get_user_password() -> str:
    password = input("Enter your password: ").strip()

    if not password:
        raise ValueError("Password cannot be empty.")

    return password


def display_results(strength: str, suggestions: List[str]) -> None:


    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nGreat! Your password meets all strength requirements.")


def main() -> None:

    checker = PasswordStrengthChecker()

    try:
        password = get_user_password()
        strength, suggestions = checker.evaluate_password(password)
        display_results(strength, suggestions)

    except ValueError as error:
        print("Input Error:", error)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    except Exception as error:  # Catch unexpected errors
        print("Unexpected Error:", error)

    finally:
        print("\nPassword check completed.")


class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):

        self.checker = PasswordStrengthChecker()

    def test_weak_password(self):

        strength, _ = self.checker.evaluate_password("abc")
        self.assertEqual(strength, "Weak")

    def test_medium_password(self):

        strength, _ = self.checker.evaluate_password("Password1")
        self.assertEqual(strength, "Medium")

    def test_strong_password(self):

        strength, _ = self.checker.evaluate_password("StrongPass1!")
        self.assertEqual(strength, "Strong")


if __name__ == "__main__":
    if "test" in sys.argv:
        unittest.main(argv=["first-arg-is-ignored"], exit=False)
    else:
        main()