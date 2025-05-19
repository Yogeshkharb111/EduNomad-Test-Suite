# 📱 EduNomad-Test-Suite 🧪

This repository contains the complete automated testing suite for the **EduNomad Android App**, built using **Appium**, **Postman**, and **JUnit**. The project verifies critical features of the EduNomad app such as user authentication, course listing, and chatbot functionality using real-world SDET practices.

> 🔍 Designed to showcase your skills for internship roles like SDET 
> 🧰 Includes UI Testing (Appium), API Testing (Postman), and Unit Testing (JUnit)

---

## 📌 Table of Contents

- [📱 Project Overview](#project-overview)
- [✅ Features Tested](#features-tested)
- [🛠️ Tools & Technologies](#tools--technologies)
- [📂 Folder Structure](#folder-structure)
- [▶️ How to Run the Tests](#how-to-run-the-tests)
- [🖼️ Screenshots](#screenshots)
- [👨‍💻 Author](#author)
- [📄 License](#license)

---

## 📱 Project Overview

**EduNomad** is an Android-based educational app designed to help users learn through video tutorials, PDFs, and AI-assisted chatbot support. Key functionalities include:

- User Sign In / Sign Up using Firebase Authentication
- Viewing Enrolled Courses
- Interacting with Gemini-powered Chatbot
- Tracking course progress

This testing suite ensures that these features work as expected, catching bugs early and improving overall app reliability.

---

## ✅ Features Tested

| Feature              | Type of Test     | Tools Used     |
|----------------------|------------------|----------------|
| Sign In / Sign Up    | UI Testing       | Appium (Python)|
| Course List Display  | UI Testing       | Appium (Python)|
| Chatbot (Gemini API) | API Testing      | Postman        |
| Input Validation     | Unit Testing     | JUnit (Kotlin) |

---

## 🛠️ Tools & Technologies

- **Appium** – Cross-platform mobile automation tool for UI testing
- **Python** – Scripting Appium tests using Selenium WebDriver
- **Postman** – API testing for Gemini chatbot and Firebase Auth
- **JUnit** – Unit testing framework in Android Studio
- **Firebase** – Authentication and Realtime Database for EduNomad app
- **Android Emulator** – To simulate testing environment

---

## 📂 Folder Structure
EduNomad-Test-Suite/
│
├── Appium/ # UI Test Scripts
│ ├── login_test.py
│ └── course_list_test.py
│
├── Postman/ # Postman API Collections
│ └── chatbot_test_collection.json
│
├── JUnit/ # Kotlin Unit Tests
│ ├── ValidationUtils.kt
│ └── ValidationUtilsTest.kt
│
├── Screenshots/ # Screenshots of test runs
│ ├── appium_login_pass.png
│ ├── postman_chatbot_success.png
│ └── junit_validation_pass.png
│
└── README.md # This file


---

## ▶️ How to Run the Tests

### 🔹 1. Appium UI Tests

1. Install dependencies:
   ```bash
   pip install Appium-Python-Client
Launch Appium Server and start Android Emulator

Navigate to the Appium/ directory and run:

bash
Copy
Edit
python login_test.py
python course_list_test.py
🔹 2. Postman API Tests
Open Postman

Import the collection:
Postman/chatbot_test_collection.json

Run the collection and check responses

🔹 3. JUnit Tests (Android Studio)
Open your EduNomad project in Android Studio

Navigate to:
EduNomad-Test-Suite/JUnit/ValidationUtilsTest.kt

Right-click and choose Run 'ValidationUtilsTest'

Launch Appium Server and start Android Emulator

Navigate to the Appium/ directory and run:

bash
Copy
Edit
python login_test.py
python course_list_test.py
🔹 2. Postman API Tests
Open Postman

Import the collection:
Postman/chatbot_test_collection.json

Run the collection and check responses

🔹 3. JUnit Tests (Android Studio)
Open your EduNomad project in Android Studio

Navigate to:
EduNomad-Test-Suite/JUnit/ValidationUtilsTest.kt

Right-click and choose Run 'ValidationUtilsTest'

🖼️ Screenshots
Appium UI Test	Postman API Test	JUnit Test

👨‍💻 Author
Yogesh
B.Tech Computer Science & Engineering | 2026
📧 yogeshkharb111@gmail.com
🔗 GitHub • LinkedIn

📄 License
This project is open-sourced under the MIT License.


