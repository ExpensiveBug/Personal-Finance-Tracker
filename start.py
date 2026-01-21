import streamlit as st
from streamlit_option_menu import option_menu


# app Background
st.markdown("""
<style>
        # remove sidebar
        [data-testid="stSidebar"] {
                display: none;
            }
        .stApp{
            background-color : #7088f5;
            }
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
            
        .stButton>button {
        width: 100%;
        border-radius: 14px;
        color: white;
        font-weight: 600;
        padding: 12px 24px;
        background-color : #0437F2;
        }
</style>""", unsafe_allow_html=True)

st.markdown("<h1 style = 'text-align:center;'> $pent count</h1>",unsafe_allow_html=True)

# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Account","Expense","Income","Report"],
    icons=["person","cash-stack","wallet2","bar-chart"],
    orientation="horizontal",
    styles={
        "container": {
            "background-color":"#0f0b05"
        },
        "nav-link":{
            "color":"#feeded"
        },
        "nav-link-selected":{
            "background-color":"#2CB58E"
        }
    }
)
# pages
if selected =="Account":
    import pages.account as a
    a.show()

elif selected == "Expense":
    import pages.expense as ep
    ep.show()

elif selected == "Income":
    import pages.income as inc
    inc.show()

elif selected == "Report":
    import pages.report as rep
    rep.show()


