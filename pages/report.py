import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import database as db

def show():
    # account login check
    if not st.session_state.logged_in:
        st.title("🔒 Login Required")
        st.warning("Please login or create account to continue")
        st.stop() 

    user_id = st.session_state.user_id

    # reporting begins 
    total_earn = 0
    total_bill = 0
    df = pd.DataFrame()
    df2 = pd.DataFrame()
    
    c1,c2 = st.columns(2)
    with c1 : 
        st.header("Bill Report")
        bill_data = db.get_bill(user_id)
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
        earn_data = db.get_income(user_id)
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


    # Now Account
    if total_earn > total_bill :
        acc = total_earn - total_bill
        st.text(f"Account Condition: ₹{acc:,.2f}")
        st.success("Account is in Profit ")

    elif total_earn < total_bill:
        acc = total_bill - total_earn
        st.text(f"Account Condition: ₹{acc:,.2f}")
        st.warning("Account is in loss ")

    else :
        acc = 0
        st.text(f"Account Condition: ₹0.00")
        st.info("No Profit No loss ")

    # creating report
    expense_df = pd.DataFrame()
    if not df.empty:
        # rename columns for normalization
        expense_df = df.copy()
        expense_df["Type"] = "Expense"
        expense_df = expense_df.reindex(columns=["Type","Category","Amount","Description"])

    income_df = pd.DataFrame()
    if not df2.empty:
        income_df = df2.rename(columns={
            "Income_type": "Category",
            "Income": "Amount",
            "Note": "Description"
        })
        income_df["Type"] = "Income"
        income_df = income_df.reindex(columns=["Type","Category","Amount","Description"])

    report_df = pd.concat([expense_df, income_df], ignore_index= True)

    if report_df.empty:
        st.info("No Data available to Download!!")
    else :
        report = report_df.to_csv(index=False)
        # Download file
        st.download_button(label="Download Report", data = report, file_name="Account_Report.csv",mime = "text/csv")  
