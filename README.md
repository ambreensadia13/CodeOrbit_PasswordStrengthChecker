# Password Strength Checker

**Cybersecurity Internship Task — CodeOrbit**

**Prepared by:** Ambreen Sadia  
**Submission Date:** 21 October 2026  
**Programming Language:** Python 3

## 1. Project Overview

The Password Strength Checker is a beginner-friendly cybersecurity project developed using Python. It evaluates a sample password based on five basic criteria and classifies its strength as Weak, Moderate, or Strong.

The program also provides suggestions to help users improve their password quality.

## 2. Project Objectives

- Understand basic password security concepts.
- Develop a password evaluation program using Python.
- Check password length and character variety.
- Display a password strength score.
- Provide feedback when security criteria are not satisfied.

## 3. Features

The program checks whether a password:

1. Contains at least 8 characters.
2. Includes uppercase letters.
3. Includes lowercase letters.
4. Contains numeric digits.
5. Includes special characters.

Each satisfied criterion adds one point to the total score.

## 4. Technologies Used

- **Python 3:** Main programming language.
- **Visual Studio Code:** Code editor.
- **Python Standard Library:** The `string` module for identifying special characters.

No third-party Python packages are required.

## 5. Project Structure

```text
CodeOrbit_PasswordStrengthChecker/
├── password_checker.py
└── README.md
```

A `screenshots` folder may also be added to store screenshots of the program's actual output.

## 6. Installation and Requirements

The following are required:

- A computer with Python 3 installed.
- Visual Studio Code or another Python editor.

Download Python from https://www.python.org/downloads/ if it is not already installed.

## 7. How to Run the Program

1. Open the project folder in Visual Studio Code.
2. Open the integrated terminal using **Terminal → New Terminal**.
3. Ensure the Python code is saved as `password_checker.py`.
4. Run the following command:

```bash
py password_checker.py
```

If the `py` command is unavailable, try:

```bash
python password_checker.py
```

5. Enter a sample password when prompted.
6. Review the score, strength classification, and improvement suggestions.

**Security precaution:** Use sample passwords for testing. Never enter your real account passwords into an educational demonstration.

## 8. Password Evaluation Method

The program evaluates five criteria and calculates a score out of five.

| Score | Strength classification |
|---|---|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

The program uses Python's built-in string methods and the `any()` function to check character types.

## 9. Test Cases

The following test cases correspond to the program's scoring logic.

| Sample password | Expected score | Expected result |
|---|---:|---|
| `hello` | 1/5 | Weak |
| `Hello123` | 4/5 | Moderate |
| `River!Cloud7` | 5/5 | Strong |

These are example test cases. Run the program to verify the results and capture screenshots for your submission.

## 10. Security Limitations

This project is an educational demonstration and does not provide a complete assessment of password security.

- It does not detect commonly used or predictable passwords.
- It does not check password databases for compromised credentials.
- It does not evaluate resistance to brute-force or dictionary attacks.
- It does not assess password reuse.
- A Strong classification does not guarantee that a password is secure.

For real accounts, use long, unique passwords or passphrases, consider a reputable password manager, and enable multi-factor authentication where available.

## 11. Future Improvements

Potential improvements include:

- Detecting common passwords using a suitable local list.
- Providing more detailed password-length guidance.
- Adding a graphical user interface.
- Implementing automated unit tests.
- Integrating a reputable password-strength estimation library.

## 12. Conclusion

The Password Strength Checker demonstrates how Python can be applied to a basic cybersecurity problem. It introduces password-quality checks, conditional logic, functions, loops, and user feedback.

The project provides a foundation for further learning in Python programming and cybersecurity.


**Project:** Password Strength Checker  
**Internship:** CodeOrbit Cybersecurity  
**Prepared by:** Ambreen Sadia  
**Submission Date:** 21 October 2026
