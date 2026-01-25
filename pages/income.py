import streamlit as st
import database as db


def create_income():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS earnings ( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   source Text,
                   amount Real,
                   note Text)
                   """)
    conn.commit()
    conn.close()

def get_income():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""Select id, source, amount, note from earnings""")
    data = cursor.fetchall()
    conn.commit()
    return data

def reset_income():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM earnings")
    conn.commit()
    conn.close()
    # reset interface
    st.session_state.income_type = "Job"
    st.session_state.amount_input = 0.0
    st.session_state.note_input = ""

def add_income():
    sal_type = st.session_state.income_type
    amt = st.session_state.amount_input
    desc = st.session_state.note_input

    if(amt <= 0):
        st.error("Amount must be greater than zero!!")
        return
    
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO earnings (source, amount, note) VALUES (?, ?, ?)",
                   (sal_type, amt, desc))
    conn.commit()
    conn.close()
    st.balloons()

    st.session_state.income_type = "Job"
    st.session_state.amount_input = 0.0
    st.session_state.note_input = ""

def show():
    # check account login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔒 Login Required")
        st.warning("Please login or create account to continue")
        st.stop() 

    # Income tracking begins
    st.set_page_config(page_title="Income Tracker", layout="centered")
    create_income()

    st.header("Income Tracker")

    st.selectbox("Select income type ",["Job","Business","Asset","Interest","Other"], key = "income_type")
    st.number_input("Amount ",min_value = 0.0, step = 100.0, key = "amount_input")
    st.text_area("Description",placeholder="Note about your income...", key = "note_input")

    st.button("Add Income",width="stretch", on_click=add_income)
    st.button("Reset",width="stretch", on_click= reset_income)


if __name__ == "__main__":
    if "income_type" not in st.session_state:
        st.session_state.income_type = "Job"
    if "amount_input" not in st.session_state:
        st.session_state.amount_type = 0.0
    if "note_input" not in st.session_state:
        st.session_state.note_input = ""
    
    show()


