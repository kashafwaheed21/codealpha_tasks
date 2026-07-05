# 🔐 Secure Coding Review

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cyber Security](https://img.shields.io/badge/Cyber%20Security-CodeAlpha-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Cyber Security Internship**.

The objective of this project is to identify security vulnerabilities in an insecure Python login system and implement secure coding practices to improve its security. A vulnerable version and a secure version of the application are provided to demonstrate the improvements.

---

## 🎯 Objectives

- Identify security vulnerabilities in a login system.
- Understand common security risks in software development.
- Apply secure coding practices.
- Compare vulnerable and secure implementations.
- Document the security improvements.

---

## ✨ Features

### Vulnerable Login System
- Username and password visible in source code (Hardcoded Credentials)
- Weak password
- Password visible while typing
- Unlimited login attempts
- No input validation

### Secure Login System
- Password hidden using `getpass`
- Limited login attempts
- Protection against brute-force attacks
- Input validation for empty fields
- Improved login flow

---

## 📂 Project Structure

```
Task-3-Secure-Coding-Review/
│
├── vulnerable_login.py
├── secure_login.py
├── Secure_Coding_Review_Report.pdf
├── README.md
└── screenshots/
    ├── Screenshot1_Successful_Login.png
    ├── Screenshot2_Invalid_Login.png
    ├── Screenshot3_Empty_Input.png
    ├── Screenshot4_Account_Locked.png
    └── Screenshot5_Source_Code.png
```

---

## 🛠️ Technologies Used

- Python 3
- VS Code
- getpass module

---

## 🔍 Vulnerabilities Identified

- Hardcoded Credentials
- Weak Password
- Password Visible While Typing
- Unlimited Login Attempts
- Lack of Input Validation

---

## 🛡️ Security Improvements

- Password masking using `getpass`
- Login attempt limitation
- Basic brute-force attack protection
- Input validation
- Improved program flow using loops and `break`

---

## ▶️ How to Run

1. Install Python 3.
2. Open the project in VS Code.
3. Run:
   - `vulnerable_login.py` to observe security weaknesses.
   - `secure_login.py` to see the improved implementation.

---

## 📸 Screenshots

Screenshots demonstrating the application's functionality are available in the **screenshots** folder.

---

## 🚀 Future Improvements

- Store credentials in a secure database.
- Implement password hashing.
- Add Two-Factor Authentication (2FA).
- Implement CAPTCHA after multiple failed login attempts.
- Maintain authentication logs for security monitoring.

---

## 👨‍💻 Author

**Kashaf Waheed**

Cyber Security Intern at CodeAlpha

---

## ⭐ Learning Outcomes

Through this project, I learned:

- Secure Coding Fundamentals
- Hardcoded Credentials
- Password Protection
- Brute-Force Attack Prevention
- Input Validation
- Secure Authentication Concepts