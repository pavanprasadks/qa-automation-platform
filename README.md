# QA Automation Platform

A scalable UI Automation Framework built using **Python**, **Playwright**, and **PyTest**, following the **Page Object Model (POM)** design pattern.

## Project Overview

This project demonstrates modern UI automation practices, including:

* Page Object Model (POM)
* Data-Driven Testing using JSON
* PyTest Fixtures
* Playwright Auto-Waiting
* Parallel Execution using pytest-xdist
* Reusable BasePage Architecture
* File Upload & Download Validation
* JavaScript Alert Handling
* Frame Handling
* Shadow DOM Automation
* Dynamic Element Testing

---

## Tech Stack

* Python 3.11
* Playwright
* PyTest
* pytest-playwright
* pytest-xdist
* JSON
* Git
* GitHub

---

## Project Structure

```text
QA Automation Platform
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── secure_page.py
│   ├── checkbox_page.py
│   ├── dropdown_page.py
│   ├── alerts_page.py
│   ├── dynamic_id_page.py
│   ├── dynamic_controls_page.py
│   ├── dynamic_loading_page.py
│   ├── frames_page.py
│   ├── file_upload_page.py
│   ├── file_download_page.py
│   ├── hover_page.py
│   ├── drag_and_drop_page.py
│   ├── multiple_windows_page.py
│   ├── shadow_dom_page.py
│   └── tables_page.py
│
├── ui_tests/
├── test_data/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Test Coverage

The framework currently automates 40+ UI test scenarios across multiple web components and workflows.

### Login

* Successful Login
* Invalid Username
* Invalid Password
* Empty Password

### Checkboxes

* Default State Validation
* Check / Uncheck Operations
* State Persistence Validation

### Dropdown

* Default Option Validation
* Option Selection
* Option Verification

### Alerts

* JavaScript Alert
* Confirm Dialog
* Prompt Dialog

### Dynamic Elements

* Dynamic Controls
* Dynamic IDs
* Dynamic Loading

### Frames

* iFrame Validation
* Email Subscription Form Validation

### File Operations

* File Upload
* File Download

### Tables

* Table Visibility Validation
* Header Validation
* Row Data Validation

### Hover Actions

* User Hover Validation
* Dynamic Caption Validation

### Multiple Windows

* Child Window Validation

### Shadow DOM

* Shadow Host Validation
* Shadow Element Interaction

---

## Installation

### Clone Repository

```bash
git clone https://github.com/pavanprasadks/qa-automation-platform.git
```

### Navigate to Project

```bash
cd qa-automation-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Execute Tests

### Run Complete Test Suite

```bash
pytest -v
```

### Run Tests in Parallel

```bash
pytest -v -n auto
```

### Run Specific Module

```bash
pytest ui_tests/test_login.py -v
```

### Run Specific Test

```bash
pytest ui_tests/test_login.py::test_login -v
```

---

## Framework Design

### Page Object Model (POM)

All page locators and page-specific actions are maintained inside dedicated Page Object classes, improving maintainability, readability, and reusability.

### BasePage

Common reusable methods include:

* Navigation
* Locator Handling
* Shared Page Actions

### Data-Driven Testing

Test data is externalized into JSON files, enabling easier maintenance and scalability.

### Fixtures

PyTest fixtures are used for:

* Browser Initialization
* Page Management
* Page Object Injection

---

## Automation Concepts Demonstrated

* UI Automation
* Assertions and Validations
* File Upload Handling
* File Download Handling
* JavaScript Dialog Handling
* Frame Automation
* Dynamic Locator Strategies
* Shadow DOM Interaction
* Data-Driven Testing
* Parallel Execution with PyTest-XDist

---
