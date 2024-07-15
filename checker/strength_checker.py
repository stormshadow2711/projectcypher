import re
from .base_strategy import PasswordStrategy

class PasswordStrengthChecker(PasswordStrategy):
    def evaluate(self, password: str) -> str:
        length = len(password)
        has_lower = re.search(r"[a-z]", password) is not None
        has_upper = re.search(r"[A-Z]", password) is not None
        has_digit = re.search(r"\d", password) is not None
        has_special = re.search(r"[!@#$%^&*()\-_=+]", password) is not None

        if length < 8:
            return "Very Weak"
        if all([has_lower, has_upper, has_digit, has_special]) and length >= 12:
            return "Very Strong"
        if length >= 8 and (has_lower or has_upper) and has_digit:
            return "Strong"
        if length >= 8 and (has_lower or has_upper):
            return "Medium"
        return "Weak"
