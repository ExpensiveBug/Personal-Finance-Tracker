import streamlit as st
import bcrypt
import database as db

# Old User account
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
                "user_id" : db_id,
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
    db.create_user_table()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.mail = None
        st.session_state.user_id = None

    # Show logout button if already logged in
    if st.session_state.logged_in:
        st.success(f"Welcome, {st.session_state.username}")
        st.write(f"Email: {st.session_state.mail}")
        if st.button("Logout", type="primary"):
            db.delete_user_data(st.session_state.user_id)
            st.session_state.clear()
            st.success("Logged out successfully")
            st.rerun()
        return 

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
                    st.session_state.user_id = user_data["user_id"]
                    st.success(f"Welcome, {st.session_state.username}")
                    st.write(f"Email : {st.session_state.mail}")
                    st.rerun()
                else : 
                    st.error("Invalid Username or Password !!")
        else:  
            st.success(f"Welcome, {st.session_state.username}")
            st.write(f"Email : {st.session_state.mail}")
            st.warning("Are you sure you want to logout?")

            if st.button("Yes, Logout"):
                db.delete_user_data(st.session_state.user_id)
                st.session_state.clear()
                st.success("Logged out successfully")
                st.rerun()

    if acnt == "Sign Up":
        user = st.text_input("Username")
        password = st.text_input("Password", type = "password")
        mail = st.text_input("E-mail",placeholder="example@gmail.com")

        if st.button("Create my account", width = "stretch"):
            if not user or not password or not mail :
                st.warning("Fill all the details !!")
            else:
                user_id = db.create_user_account(user, password, mail)
                if user_id : 
                    st.snow()
                    st.session_state.logged_in = True
                    st.session_state.username = user
                    st.session_state.mail = mail
                    st.session_state.user_id = user_id
                    st.success("Yeah, Account created Succesfully :)")
                    st.success(f"Welcome, {user}")
                    st.write(f"Email : {mail}")
                    st.rerun()

                else : 
                    st.error("Username or email already exist !!")

