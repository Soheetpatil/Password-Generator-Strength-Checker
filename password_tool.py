import secrets
import string
import sys


class PasswordTool:
    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.special = string.punctuation

    def generate_password(self, length, use_upper, use_lower, use_digits, use_special):
        char_pool = ""
        required_chars = []

        if use_upper:
            char_pool += self.uppercase
            required_chars.append(secrets.choice(self.uppercase))
        if use_lower:
            char_pool += self.lowercase
            required_chars.append(secrets.choice(self.lowercase))
        if use_digits:
            char_pool += self.digits
            required_chars.append(secrets.choice(self.digits))
        if use_special:
            char_pool += self.special
            required_chars.append(secrets.choice(self.special))

        if not char_pool:
            raise ValueError("At least one character type must be selected")

        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]
        
        secrets.SystemRandom().shuffle(password_chars)
        return ''.join(password_chars)

    def check_strength(self, password):
        score = 0
        reasons = []
        suggestions = []

        if not password:
            return "Invalid", [], ["Password cannot be empty"]

        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.special for c in password)
        length = len(password)

        if length >= 12:
            score += 2
            reasons.append("Length is 12 characters or more")
        elif length >= 8:
            score += 1
            reasons.append("Length is 8-11 characters")
        else:
            suggestions.append("Increase password length to at least 8 characters, preferably 12+")

        if has_upper:
            score += 1
            reasons.append("Contains uppercase letters")
        else:
            suggestions.append("Add uppercase letters")

        if has_lower:
            score += 1
            reasons.append("Contains lowercase letters")
        else:
            suggestions.append("Add lowercase letters")

        if has_digit:
            score += 1
            reasons.append("Contains numbers")
        else:
            suggestions.append("Add numbers")

        if has_special:
            score += 1
            reasons.append("Contains special characters")
        else:
            suggestions.append("Add special characters like !@#$%^&*")

        if score >= 6:
            strength = "Strong"
        elif score >= 4:
            strength = "Medium"
        else:
            strength = "Weak"

        return strength, reasons, suggestions


def get_valid_integer(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"\n  [ERROR] Please enter a number greater than or equal to {min_val}\n")
                continue
            if max_val is not None and value > max_val:
                print(f"\n  [ERROR] Please enter a number less than or equal to {max_val}\n")
                continue
            return value
        except ValueError:
            print("\n  [ERROR] Please enter a valid integer\n")


def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print("\n  [ERROR] Please enter 'y' or 'n'\n")


def display_menu():
    print("\n" + "="*40)
    print("    Password Generator & Strength Checker")
    print("="*40)
    print("1. Quick Generate (12 chars, all types)")
    print("2. Custom Generate Password")
    print("3. Check Password Strength")
    print("4. Exit")
    print("="*40)


def main():
    tool = PasswordTool()

    while True:
        display_menu()
        choice = get_valid_integer("\nEnter your choice (1-4): ", 1, 4)

        if choice == 1:
            print("\n" + "-"*40)
            print("          Quick Generate")
            print("-"*40)
            try:
                password = tool.generate_password(12, True, True, True, True)
                print(f"\nGenerated Password: {password}")
                
                strength, reasons, suggestions = tool.check_strength(password)
                print("\n" + "="*40)
                print(f"Password Strength: {strength}")
                print("="*40)
                if reasons:
                    print("\nReasons:")
                    for reason in reasons:
                        print(f"  • {reason}")
                if suggestions:
                    print("\nSuggestions for improvement:")
                    for suggestion in suggestions:
                        print(f"  • {suggestion}")
                print("\n" + "-"*40)
            except ValueError as e:
                print(f"\nError: {e}")

        elif choice == 2:
            print("\n" + "-"*40)
            print("         Custom Generate")
            print("-"*40)
            length = get_valid_integer("Enter password length (minimum 4): ", 4)
            use_upper = get_yes_no("Include uppercase letters? (y/n): ")
            use_lower = get_yes_no("Include lowercase letters? (y/n): ")
            use_digits = get_yes_no("Include numbers? (y/n): ")
            use_special = get_yes_no("Include special characters? (y/n): ")

            try:
                password = tool.generate_password(length, use_upper, use_lower, use_digits, use_special)
                print(f"\nGenerated Password: {password}")
                
                strength, reasons, suggestions = tool.check_strength(password)
                print("\n" + "="*40)
                print(f"Password Strength: {strength}")
                print("="*40)
                if reasons:
                    print("\nReasons:")
                    for reason in reasons:
                        print(f"  • {reason}")
                if suggestions:
                    print("\nSuggestions for improvement:")
                    for suggestion in suggestions:
                        print(f"  • {suggestion}")
                print("\n" + "-"*40)
            except ValueError as e:
                print(f"\nError: {e}")

        elif choice == 3:
            print("\n" + "-"*40)
            print("      Password Strength Checker")
            print("-"*40)
            password = input("Enter the password to check: ").strip()

            strength, reasons, suggestions = tool.check_strength(password)
            print("\n" + "="*40)
            print(f"Password Strength: {strength}")
            print("="*40)
            if reasons:
                print("\nReasons:")
                for reason in reasons:
                    print(f"  • {reason}")
            if suggestions:
                print("\nSuggestions for improvement:")
                for suggestion in suggestions:
                    print(f"  • {suggestion}")
            print("\n" + "-"*40)

        elif choice == 4:
            print("\nThank you for using Password Generator & Strength Checker!")
            sys.exit(0)


if __name__ == "__main__":
    main()
