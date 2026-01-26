# Personal-Finance-Tracker

### Description 
This is a user-friendly Streamlit personal finance tracker app that help user to manage their money easily. User can add, edit, or delete income and spending transactions. The app tracks user finances and generates detailed reports with clear insights into user spending habits, helping user to understand where their money goes and make better financial decisions.

## Installation
pip install -r requirements.txt

## Run the App
streamlit run start.py

### Features
- [User Account](#user-account)
- [Go to Expense Tracking](#Expense-Tracking)
- [Go to Income Management](#Income-Management)
- [Go to Visual Reports](#Visual-Reports)
- [Go to Secure password handling](#Secure-Password-handling)

## User Account :
<img width="927" height="267" alt="image" src="https://github.com/user-attachments/assets/cc3d5096-7b1f-4944-8a39-6c700ff9f2f4" />
Here, we can create a new account by clicking the sign up button and login to already existing account
Without an account we cannot move forward to use the app

## Expense Tracking
The app allows users to record their expenses effortlessly. Users can:

- Choose the type of expense (e.g., Food, Travel, Entertainment, Electronics, Miscellaneous)
- Enter the amount spent
- Add a short description to keep track of what the expense was for
- Edit or delete previous entries

This helps users monitor their spending habits and identify areas where they can save money.

**Example:**  
_A user spends $50 on groceries and adds a note: “Weekly groceries at SuperMart.”_

## Income Management
Users can also track all sources of income. The app allows:

- Selecting income type (Job, Business, Assets, Interest, Other)
- Adding the income amount
- Writing a short note for context (e.g., “Freelance project payment”)
- Viewing and updating previous income records

This helps users compare their income vs expenses and see their net balance over time.

## Visual Reports
<img width="1265" height="923" alt="image" src="https://github.com/user-attachments/assets/f0deadfd-ddcb-4b9b-be1a-76bb03f5989e" />
The Visual Reports section displays a summary of all recorded expenses and income.
The app calculates the net balance to determine whether the user is in a loss or profit.

## Secure Password handling 
Passwords are hashed using bcrypt to ensure secure storage:
```python
hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```
Password will be verified with : 
```python
  bcrypt.checkpw(entered_password.encode(), stored_hashed_pw)
```
