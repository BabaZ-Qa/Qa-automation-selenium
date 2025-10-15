Project: Login Page Automation Test (Demo Website)
Author: Babazahid Zayidov
Tools: Python, Selenium, Pytest, DDT, POM (Page Object Model)

About the Project:

This project automates the login functionality of a demo website.
It includes tests for valid and invalid login scenarios using 
Python with Selenium WebDriver and the Pytest framework.

The goal of this project is to demonstrate how a QA Automation 
Engineer can design structured, data-driven tests by following 
the Page Object Model (POM) pattern. 


What This Test Covers:

1. Invalid Username → Expected message: "Your username is invalid!"
2. Invalid Password → Expected message: "Your password is invalid!"
3. Valid Login → Expected message: "Logged In Successfully"

All these scenarios are tested automatically using DDT (data-driven testing)
so that the same test logic runs with different input data.

Project Structure:

UI-Tests/
│
├── TestPracticePages/
│   └── Homepage.py       # Page Object file with locators and actions
│
├── TestPractice/
│   └── test_practice_login.py  # Main test file
│
├── conftest.py           # Setup and teardown configuration
│
└── README.txt


How to Run the Tests:

1. Run the tests with:
   pytest -v --html=report.html

2. The test results will appear in the terminal 
   and an HTML report will be generated.


Technologies Used:

- Python
- Selenium WebDriver
- Pytest Framework
- DDT (Data Driven Testing)
- POM (Page Object Model)
- HTML Reports (pytest-html)


Contact:

LinkedIn: [www.linkedin.com/in/babazahid-zayidov-a5a1b0384]
GitHub: [https://github.com/BabaZ-Qa]
Email: [Zahidzahidli430@gmail.com]

Notes:

This project was fully created by me from scratch as part of my
QA Automation learning journey. It reflects my current knowledge
of Python, Selenium, and test framework design.