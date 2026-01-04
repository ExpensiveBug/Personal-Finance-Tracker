import streamlit as st

def show():
    st.header("Income Tracker")
    sourse = st.selectbox("Select income type ",["Salary","Business","Asset","Interest","Other"])
    amt = st.number_input("Amount ",min_value = 0)
    note = st.text_area("Description",value="Note something about your income...")

    if st.button("Add Income",width="stretch"):
        if sourse and amt :
            pass
        else : 
            st.error("Fill the above details first !!")
    if st.button("Reset",width="stretch"):
        pass