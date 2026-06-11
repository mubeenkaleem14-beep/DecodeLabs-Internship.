
import string

def check_password_strength(password: str) -> str:
    length = len(password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(ch in string.punctuation for ch in password)
    if length < 6:
        return "Weak → Too short (minimum 6 characters)."
    elif length >= 8 and has_upper and has_digit and has_symbol:
        return "Strong → Great mix of length, uppercase, numbers, and symbols."
    elif length >= 6 and (has_upper or has_digit or has_symbol):
        return "Medium → Decent password, but could be stronger."
    else:
        return "Weak → Needs uppercase, numbers, or symbols."
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print("Password Strength →", check_password_strength(pwd))
