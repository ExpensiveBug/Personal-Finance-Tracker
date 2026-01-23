import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pages.expense import get_bill             # to look expense.py in same folder
from pages.income import get_income

def show():
    # account login check
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔒 Login Required")
        st.warning("Please login or create account to continue")
        st.stop() 

    # reporting begins 
    total_earn = 0
    total_bill = 0
    c1,c2 = st.columns(2)
    with c1 : 
        st.header("Bill Report")
        bill_data = get_bill()
        if bill_data:
            df = pd.DataFrame(bill_data, columns=["ID", "Category", "Amount", "Description"])
            st.dataframe(df.drop(columns=["ID"]), width="content")
            
            total_bill = df["Amount"].sum()
            st.text(f"Total Expenses ₹{total_bill:,.2f}")

            fig, ax = plt.subplots(figsize = (8,5))
            bars = ax.bar(df["Category"], df["Amount"], width=0.3, color = ['blue', 'red', 'orange'])
            ax.bar_label(bars,padding=3)
            ax.set_title("Amount vs Expense")
            st.pyplot(fig)

        else:
            st.info("No expenses recorded yet.")      
    
    with c2 : 
        st.header("Income Report")
        earn_data = get_income()
        if earn_data :
            df2 = pd.DataFrame(earn_data, columns=["ID","Income_type", "Income", "Note"])
            st.dataframe(df2.drop(columns=["ID"]), width="content")

            total_earn = df2["Income"].sum()
            st.text(f"Total Income ₹{total_earn:,.2f}")

            fig,ax = plt.subplots(figsize=(8,5))
            bars = ax.bar(df2["Income_type"], df2["Income"],  width = 0.3, color = ["#63B0F3","#394FE0","#3B2EF2"])
            ax.bar_label(bars, padding=1)
            ax.set_title("Income vs Source")
            st.pyplot(fig)

        else : 
            st.info("No Income recorded yet.")


    if total_bill and total_earn:
        acc = total_earn-total_bill
        st.text(f"📊 Account Condition: ₹{acc:,.2f}")
    elif total_earn :
        acc = total_earn
        st.text(f"📊 Account Condition: ₹{acc:,.2f}")
