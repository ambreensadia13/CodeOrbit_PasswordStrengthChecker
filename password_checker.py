
import string


def check_password(password):
    """Evaluate a password using five basic security checks."""

    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains uppercase letters": any(c.isupper() for c in password),
        "Contains lowercase letters": any(c.islower() for c in password),
        "Contains numbers": any(c.isdigit() for c in password),
        "Contains special characters": any(
            c in string.punctuation for c in password
        ),
    }

    score = sum(checks.values())

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return checks, score, strength


def main():
    print("=" * 42)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 42)
    print("Educational cybersecurity project")
    print("Use a sample password, not your real password.\n")

    password = input("Enter a sample password: ")

    checks, score, strength = check_password(password)

    print("\n--- Password Analysis ---")

    for criterion, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{criterion}: {status}")

    print(f"\nScore: {score}/5")
    print(f"Password Strength: {strength}")

    if score < 5:
        print("\nSuggestions for improvement:")
        for criterion, passed in checks.items():
            if not passed:
                print(f"- {criterion}")

    print("\nNote: This is a basic educational checker.")
    print("It does not test against leaked or common passwords.")


if __name__ == "__main__":
    main()

