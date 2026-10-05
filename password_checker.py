import re

print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

# Check password requirements
length_check = len(password) >= 8
uppercase_check = bool(re.search(r"[A-Z]", password))
number_check = bool(re.search(r"[0-9]", password))
special_check = bool(re.search(r"[^A-Za-z0-9]", password))

print("\nPassword Analysis")
print("----------------------------")

print("Minimum 8 characters :", "PASS" if length_check else "FAIL")
print("Uppercase letter     :", "PASS" if uppercase_check else "FAIL")
print("Number               :", "PASS" if number_check else "FAIL")
print("Special character    :", "PASS" if special_check else "FAIL")

# Check final password strength
if length_check and uppercase_check and number_check and special_check:
    print("\nPassword Strength: STRONG")
    print("Your password satisfies all requirements.")
else:
    print("\nPassword Strength: WEAK")
    print("Please improve your password.")

    if not length_check:
        print("- Use at least 8 characters.")

    if not uppercase_check:
        print("- Add at least one uppercase letter (A-Z).")

    if not number_check:
        print("- Add at least one number (0-9).")

    if not special_check:
        print("- Add at least one special character.")