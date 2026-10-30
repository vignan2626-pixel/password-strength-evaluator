import re

def evaluate_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append(" Add at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" Add at least one number (0-9).")

    # Special character check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append(" Add at least one special character (e.g., @, $, !, %, *, ?, &).")

    # Determine strength rating
    print("\n" + "="*40)
    print(f"Password Evaluated: {'*' * len(password)}")
    print("="*40)

    if score == 5:
        print("Strength: EXTREMELY STRONG! Your password is secure.")
    elif score >= 4:
        print("Strength: STRONG. Good job, but could be safer.")
    elif score >= 3:
        print("Strength: MODERATE. Consider adding more security elements.")
    else:
        print("Strength: WEAK. Your password can be easily cracked.")

    if feedback:
        print("\nSuggestions for improvement:")
        for item in feedback:
            print(f"  {item}")
    print("="*40 + "\n")

if __name__ == "__main__":
    print("Welcome to the Password Strength Evaluator!")
    user_password = input("Enter a password to test: ")
    evaluate_password(user_password)
