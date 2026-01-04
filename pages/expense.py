import streamlit as st

def show():
    st.subheader("Expense Tracker")
    expense = st.selectbox("Select the type of expense",["Food","Entertainment","Travel","Fuel","Electronics","Miscellaneous"])
    amt = st.number_input("Amount",min_value = 0)

    des = st.text_area("Description",value = "Tell something about your expense")

    if st.button("Add Expense",width="stretch"):
        if expense and amt:
            pass
        else : 
            st.error("First Enter your Expense data !!")
    if st.button("Reset",width="stretch"):
        pass