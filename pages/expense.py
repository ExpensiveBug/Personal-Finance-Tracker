import streamlit as st
import database as db
import pandas as pd

# Create Bill 
def create_table():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

# Getting Bill
def get_bill():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, amount, description FROM expenses")
    data = cursor.fetchall()
    conn.close()
    return data

# Add to cart
def add_expense():
    # Fetch values directly from session state 
    cat = st.session_state.category_input
    amt = st.session_state.amount_input
    desc = st.session_state.desc_input

    if amt <= 0:
        st.error("Amount must be greater than 0!")
        return

    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
        (cat, amt, desc)
    )
    conn.commit()
    conn.close()
    
    # Reset session state
    st.session_state.category_input = "Food"
    st.session_state.amount_input = 0.0
    st.session_state.desc_input = ""
    st.balloons()


def reset_all():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses")
    conn.commit()
    conn.close()
    # Reset session state
    st.session_state.category_input = "Food"
    st.session_state.amount_input = 0.0
    st.session_state.desc_input = ""
    st.balloons()

    

# main function 
def show():
    # check account login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔒 Login Required")
        st.warning("Please login or create account to continue")
        st.stop() 

    # expense tracking begins
    st.set_page_config(page_title="Expense Tracker", layout="centered")
    st.title("Personal Expense Tracker")
    create_table()

    # Form Inputes
    st.selectbox(
        "Select the type of expense",
        ["Food", "Entertainment", "Travel", "Fuel", "Electronics", "Miscellaneous"],
        key="category_input"
    )
    st.number_input("Amount", min_value=0.0, step=100.0, key="amount_input")

    st.text_area("Description", placeholder="What was this for?", key="desc_input")

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        st.button("Add Expense", width="stretch", on_click=add_expense, type="primary")

    with col2:
        st.button("Reset All Data", width="stretch", on_click=reset_all)

if __name__ == "__main__":
    # Initialize session state keys if they don't exist
    if "category_input" not in st.session_state:
        st.session_state.category_input = "Food"
    if "amount_input" not in st.session_state:
        st.session_state.amount_input = 0.0
    if "desc_input" not in st.session_state:
        st.session_state.desc_input = ""

    show()

