import streamlit as st

def show():
    st.header("Create Your :green[Account]")

    acnt = st.radio("Account",["Login", "Sign Up"])
    if acnt == "Login":
        
        user = st.text_input("Username",key="u_name")
        password = st.text_input("Password", type = "password",key= "entry_gate")
        if st.button("Login", width="stretch"):
            if user and password :
                st.balloons()
            else :
                st.warning("Fill all the above details !!")

    if acnt == "Sign Up":
        
        user = st.text_input("Username")
        password = st.text_input("Password", type = "password")
        mail = st.text_input("E-mail",placeholder="example@gmail.com")

        if st.button("Create my account", width = "stretch"):
            if user and password and mail :
                st.snow()
            else : 
                st.warning("Fill all the details !!")

