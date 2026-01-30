# ✈️ Airline Booking System

A simple **Airline Booking System** designed to demonstrate core software engineering and DevOps concepts using **Python**, **Git**, and **GitHub**. This project focuses on clean repository practices, issue tracking, and CI automation with GitHub Actions.

---

## 📌 Project Overview

The Airline Booking System allows users to:

* View available flights
* Make flight bookings
* Manage booking-related operations

This repository is also used to demonstrate:

* Proper GitHub repository structure
* Use of `.gitignore` to avoid cache files
* Issue-based development
* Continuous Integration using GitHub Actions

---

## 🛠️ Tech Stack

* **Language:** Python 3.11
* **Version Control:** Git & GitHub
* **CI/CD:** GitHub Actions
* **Tools:** VS Code

---

## 📂 Project Structure

```
AirlineBookingSystem/
│
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    └── main.py
```

---

## 🚀 How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/Mahamfatyma889/AirlineBookingSystem.git
   ```

2. Navigate to the project folder

   ```bash
   cd AirlineBookingSystem
   ```

3. (Optional) Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application

   ```bash
   python src/main.py
   ```

---

## ⚙️ GitHub Actions (CI)

This project includes a **GitHub Actions CI workflow** that:

* Runs automatically on every push and pull request
* Sets up Python environment
* Verifies Python version

✔ This ensures the project builds correctly and follows CI best practices.

---

## 🐞 Issue Tracking

All development tasks and improvements are tracked using **GitHub Issues**.

* Issues are created for each feature or fix
* Commits are linked to issues using `fixes #issue_number`

This demonstrates real-world collaborative development workflow.

---

## 🧹 Repository Best Practices

* Cache files removed (`__pycache__`, `node_modules`, etc.)
* `.gitignore` properly configured
* Clean and readable commit history

---

## 👩‍💻 Author

**Maham Fatyma**
Software Engineering Student
Learning DevOps, CI/CD & Cloud Technologies

---

## 📄 License

This project is for **educational purposes only**.
