import streamlit as st
import pandas as pd
import random
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from kriptoRSA.pages.util import gen_keypair, RSA_encrypt

bg = """
<style>
.appview-container {
    background-color: #f1f1ff;
    background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #f1f1ff 17px ), repeating-linear-gradient( #c6cbff55, #c6cbff );
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""


st.markdown(bg, unsafe_allow_html=True)

# 3 section : generate keypair, encrypt, decrypt
# input : foto sama key

# set word
st.title('RSA Photo Encryptor')
st.write('by Kelompok 8 : Angel, Cindy, Helen, Stacia, Stella')

st.header('Untuk memulai mari coba masukkan sebuah gambar')


# upload image
user_file = st.file_uploader("Masukkan sebuah gambar :sunglasses:", ['png', 'jpg'])


if user_file is not None:
    # show original
    st.image(user_file, use_column_width=True)

  

    

# load classifier

# load class name

# display image
    
# classify image
    
# send encrypt
    


