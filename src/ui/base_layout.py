import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #5865F2, #8EA6FF) !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: rgba(255,255,255,0.85) !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #E0E3FF, #FFFFFF) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

        /* Hide Top Bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;    
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            background: linear-gradient(90deg, #5865F2, #EB459E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #5865F2;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;    
            color: #333333;
        }

        button {
            border-radius: 1rem !important;
            background: linear-gradient(135deg, #5865F2, #8EA6FF) !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
        }

        button[kind="secondary"] {
            border-radius: 1rem !important;
            background: linear-gradient(135deg, #EB459E, #FF9ECD) !important;
            color: white !important;
        }

        button[kind="tertiary"] {
            border-radius: 1rem !important;
            background: linear-gradient(135deg, #000000, #333333) !important;
            color: white !important;
        }

        button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)
