import streamlit as st
import sqlite3
import bcrypt

def get_connection():
    return sqlite3.connect("PersonalFinance.db")

# Account
# user's table
def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    # user table
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_record(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password BLOB)
                    """)
    conn.commit()
    conn.close()
    

# create New user
def create_user_account(username, password, mail):
    conn = get_connection()
    cursor = conn.cursor()
    # check if user already exist
    cursor.execute("Select 1 FROM users_record WHERE username = ?",(username,))
    if cursor.fetchone():
        conn.close()
        return False
        
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO users_record (username, password, email) VALUES (?, ?, ?)",(username, hashed_pw, mail))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return True

# verify Old User account 
def user_verify(user, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password, email FROM users_record WHERE username = ?",
                   (user,)  )
    result = cursor.fetchone()
    conn.close()

    if result:
        db_id, db_user, db_password, db_mail = result
        if bcrypt.checkpw(password.encode(), db_password):
            return {

                "username" : db_user,
                "email" : db_mail
            }
        else:
            st.error("Invalid Password!!")
            return None
    else:
        st.error("User not found :( ")
        return None

# Expense 
# Bill table
def create_bill_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    category TEXT,
                    amount REAL,
                    description TEXT,
                    FOREIGN KEY(user_id) REFERENCES users_record(id))
                   """)
    conn.commit()
    conn.close()

# get bill
def get_bill(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, amount, description FROM expenses WHERE user_id = ?", (user_id,))
    data = cursor.fetchall()
    conn.close()
    return data

# Income
# income table
def create_income_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS earnings ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    source Text,
                    amount Real,
                    note Text,
                    FOREIGN KEY(user_id) REFERENCES users_record(id))
                   """)

    conn.commit()
    conn.close()
    conn.close()

def get_income(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("Select id, source, amount, note from earnings WHERE user_id == ? ", (user_id,))
    data = cursor.fetchall()
    conn.commit()
    return data


# Delete all user data on logout
def delete_user_data(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM earnings WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM expenses WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

