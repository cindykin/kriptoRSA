import streamlit as st

def style() :
    custom = """
    <style>
    .appview-container {
        background-color: #f1f1ff;
        background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #f1f1ff 17px ), repeating-linear-gradient( #c6cbff55, #c6cbff );
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    [data-testid="stSidebar"], [data-testid="stDecoration"] {
        display: none;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """
    st.markdown(custom, unsafe_allow_html=True)

    
    st.markdown(
        """
        <h1 style='text-align: center;'>RSA Mini but Powerful</h1>
        <div style='text-align: center;'>by Kelompok 8 Kripto : Angel, Cindy, Helen, Stacia, Stella</div><br><br><br>
        """, unsafe_allow_html=True)

