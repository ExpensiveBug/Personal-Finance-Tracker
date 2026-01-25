import streamlit as st
import database as db
import bcrypt

def users_table():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_record(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL
                    )""")
    conn.commit()
    conn.close()

def create_user(username, password, mail):
    conn = db.get_connection()
    cursor = conn.cursor()
    # check if user already exist
    cursor.execute("Select 1 FROM users_record WHERE username = ? and email = ?",
                   (username, mail))
    if cursor.fetchone():
        conn.close()
        return False
    
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO users_record (username, password, email) VALUES (?, ?, ?)",(username, hashed_pw, mail))
    conn.commit()
    conn.close()
    return True

def user_verify(user, password):
    conn = db.get_connection()
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

# main function
def show():
    st.header("Create Your :green[Account]")
    users_table()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.mail = None

    acnt = st.pills("Account",["Login", "Sign Up"],selection_mode="single")

    if acnt == "Login":
        if not st.session_state.logged_in:
            user = st.text_input("Username",key="u_name")
            password = st.text_input("Password", type = "password",key= "entry_gate")

            if st.button("Login", width="stretch"):
                user_data = user_verify(user, password)
                if user_data:
                    st.balloons()
                    st.session_state.logged_in = True
                    st.session_state.username = user_data["username"]
                    st.session_state.mail = user_data["email"]
                    st.success(f"Welcome, {st.session_state.username} 👋")
                    st.write(f"Email : {st.session_state.mail}")
                    st.rerun()
                else : 
                    st.error("Invalid Username or Password !!")
        else:  
            st.success(f"Welcome, {st.session_state.username}")
            st.write(f"Email : {st.session_state.mail}")
            st.info("Are you sure you want to logout?")

            if st.button("Yes, Logout"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.mail = None
                st.success("Logged out successfully")
                st.rerun()

    if acnt == "Sign Up":
        user = st.text_input("Username")
        password = st.text_input("Password", type = "password")
        mail = st.text_input("E-mail",placeholder="example@gmail.com")

        if st.button("Create my account", width = "stretch"):
            if not user or not password or not mail :
                st.warning("Fill all the details !!")
            elif create_user(user, password, mail) : 
                st.snow()
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.mail = mail
                st.success("Yeah, Account created Succesfully :)")
                st.success(f"Welcome, {user}")
                st.write(f"Email : {mail}")

            else : 
                st.error("Username or email already exist !!")


