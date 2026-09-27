# ECommerce Selenium Automation Framework

VIdeo demostration link: https://drive.google.com/file/d/1x2rV23b_WpXHQXZ_vTxTh1eyxhPVWQVF/view?usp=sharing

## Project Overview

This project is a Selenium-based automation framework developed in Python for testing an e-commerce web application.

The framework automates:

- User Login
- Product Search
- Data-driven product search testing
- Screenshot capture on test failure
- HTML test reporting

The project uses Page Object Model (POM), PyTest, Unittest, configuration management, utility classes, and CSV-based test data.

---

## Application Under Test

AutomationExercise

URL:

https://automationexercise.com/

---

## Technologies Used

- Python
- Selenium WebDriver
- PyTest
- Unittest
- Page Object Model (POM)
- pytest-html
- WebDriver Manager
- CSV
- python-dotenv
- ConfigParser
- Git and GitHub

---

## Project Structure

```text
ECommerce_Capstone/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   └── products_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_product_search.py
│   └── test_unittest_login.py
│
├── test_data/
│   └── product_data.csv
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   └── screenshot.py
│
├── reports/
├── screenshots/
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


