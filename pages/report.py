import streamlit as st

def show():
    st.title("Report")
    # st.write("Here show the dataframe in which all the details are stored")
    st.write("Date | Month | Category | Type | Amount | Description")

    st.header("Data")
    st.write("Plot amount vs Expense Type Barplot ")
    st.write("Plot Amount vs salary Barplot")

    st.success("Total Income : Rs")
    st.error("Total Expenses : Rs")
    st.success("Total Balance : Rs")    # if positive else st.error