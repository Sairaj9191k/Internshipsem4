import re
import hashlib

# Common weak passwords list
common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

# Old passwords (for reuse prevention)
old_passwords_hashed = [
    hashlib.sha256("Siddhu@123".encode()).hexdigest(),
    hashlib.sha256("Hello@2024".encode()).hexdigest(),
]


# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Common password check
    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords")

    return score, suggestions


# Function to classify strength
def get_strength(score):
    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Medium ⚠"
    else:
        return "Strong ✅"


# Function to generate strong password suggestion
def generate_suggestion(password):
    suggestion = password

    if not re.search(r"[A-Z]", suggestion):
        suggestion += "A"

    if not re.search(r"[a-z]", suggestion):
        suggestion += "a"

    if not re.search(r"[0-9]", suggestion):
        suggestion += "1"

    if not re.search(r"[!@#$%^&*]", suggestion):
        suggestion += "@"

    if len(suggestion) < 8:
        suggestion += "Xy9@"

    return suggestion


# ================= MAIN PROGRAM =================

password = input("Enter your password: ")

# Hash the password
hashed = hash_password(password)

# Check reuse
if hashed in old_passwords_hashed:
    print("❌ You have already used this password. Try a new one.")
else:
    score, suggestions = check_password_strength(password)
    strength = get_strength(score)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print("-", s)

    # Generate stronger suggestion
    strong_pass = generate_suggestion(password)
    print("\nSuggested Strong Password:", strong_pass)

    # Show hashed password (for learning purpose)
    print("\nHashed Password (SHA-256):", hashed)
