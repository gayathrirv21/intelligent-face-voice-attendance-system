import streamlit as st

def footer_home():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center">
            <p style="font-weight:600; color:white; margin:0;">Created with ❤️ by Gayathri</p>  
            <img src='https://cdn-icons-png.flaticon.com/512/29/29302.png' style='max-height:24px;' />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center">
            <p style="font-weight:600; color:#333; margin:0;">Created with ❤️ by Gayathri</p>  
            <img src='https://cdn-icons-png.flaticon.com/512/29/29302.png' style='max-height:24px;' />
        </div>
    """, unsafe_allow_html=True)
