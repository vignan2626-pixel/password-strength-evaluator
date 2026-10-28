import random
import string

def evaluate_password(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make the password at least 8 characters long.")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
        
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")
        
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include at least one special symbol (!@#$%^&*).")
        
    print(f"\n--- Evaluation Results ---")
    print(f"Strength Score: {score}/5")
    
    if score == 5:
        print("Rating: Strong & Secure 🔒")
    elif score >= 3:
        print("Rating: Moderate ⚠️")
    else:
        print("Rating: Weak ❌")
        
    if feedback:
        print("\nRecommendations to improve:")
        for tip in feedback:
            print(f" - {tip}")

def generate_secure_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    secure_pwd = "".join(random.choice(chars) for _ in range(length))
    print(f"\nGenerated Secure Password: {secure_pwd}")

def main():
    while True:
        print("\n=== Project 6005: Password Strength Evaluator ===")
        print("1. Evaluate a Password")
        print("2. Generate a Secure Password")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        if choice == '1':
            pwd = input("Enter password to evaluate: ")
            evaluate_password(pwd)
        elif choice == '2':
            generate_secure_password()
        elif choice == '3':
            print("Exiting Evaluator. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
