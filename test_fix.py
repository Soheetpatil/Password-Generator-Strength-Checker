import sys
sys.path.insert(0, 'd:\\Soheet project\\python\\Password-Generator-Strength-Checker')

from password_tool import PasswordTool

tool = PasswordTool()

print("Testing empty password:")
strength, reasons, suggestions = tool.check_strength("")
print(f"Strength: {strength}")
print(f"Reasons: {reasons}")
print(f"Suggestions: {suggestions}")

print("\nTesting password 'test':")
strength, reasons, suggestions = tool.check_strength("test")
print(f"Strength: {strength}")
print(f"Reasons: {reasons}")
print(f"Suggestions: {suggestions}")

print("\nTesting strong password:")
strength, reasons, suggestions = tool.check_strength("Test123!@#")
print(f"Strength: {strength}")
print(f"Reasons: {reasons}")
print(f"Suggestions: {suggestions}")
