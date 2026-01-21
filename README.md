# Personal-Finance-Tracker

### Description 
This is a user-friendly Streamlit personal finance tracker app that help user's to manage their money easily. User can add, edit, or delete income and spending transactions. The app tracks user finances and generates detailed reports with clear insights into user spending habits, helping user to understand where his/her money goes and make better financial decisions.

### Features
- [Go to User Account](#User Account(Login/ sign up))
- [Go to Expense Tracking](#Expense Tracking)
- [Go to Income Management](#Income Management)
- [Go to Visual Reports](#Visual Reports)
- [Go to Secure password handling](#Secure Password handling (bcrypt))

## User Account(Login/ Sign Up :
<img width="927" height="267" alt="image" src="https://github.com/user-attachments/assets/cc3d5096-7b1f-4944-8a39-6c700ff9f2f4" />
Here, we can create a new account by clicking the sign up button and login to already existing account
Without an account we cannot move forward to use the app

## Expense Tracking
```st.selectbox(
        "Select the type of expense",
        ["Food", "Entertainment", "Travel", "Fuel", "Electronics", "Miscellaneous"],
        key="category_input"
    )
    st.number_input("Amount", min_value=0.0, step=100.0, key="amount_input")

    st.text_area("Description", placeholder="What was this for?", key="desc_input")
```
we track the expense by selecting the given option and adding the amount we have spent on it, also we can add description about the expense.

## Income Management
```st.header("Income Tracker")

    st.selectbox("Select income type ",["Job","Business","Asset","Interest","Other"], key = "income_type")
    st.number_input("Amount ",min_value = 0.0, step = 100.0, key = "amount_input")
    st.text_area("Description",placeholder="Note about your income...", key = "note_input")

    st.button("Add Income",width="stretch", on_click=add_income)
    st.button("Reset",width="stretch", on_click= reset_income)
```
Here we insert our income and source of that income and also we can add some Note about the income. 

## Visual Reports
// image
Here we see the expenses bills report that were added earlier and also the income report.
then we calculate our account situation whether it's in lose or still have some positive amount.

## Secure Password handling (bcrypt)
code
