import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from kriptoRSA.pages.util import gen_keypair
from style import style

st.set_page_config(
    page_title="RSA Mini but Powerful",
    page_icon="✨",
)

style()



st.header(":rainbow[Generate Random Key Pair]")
st.write('Untuk memulai, coba dapatkan pasangan kunci yang telah kami persiapkan')
btn1 = st.button(":shamrock: Dapatkan Key Pair!")

if btn1:
    st.write('Ini keynya jangan lupa dicatat ya!')
    e, d, n = gen_keypair()
    st.markdown(
        f"""
        <div style="display: inline; font-size: 110%; font-weight: bold; color: #006cff">Public Key (e)&nbsp;&nbsp;&nbsp;=&nbsp;&nbsp;</div>{e} <br>
        <div style="display: inline; font-size: 110%; font-weight: bold; color: #006cff">Private Key (d)&nbsp;=&nbsp;&nbsp;</div>{d} <br>
        <div style="display: inline; font-size: 110%; font-weight: bold; color: #006cff">Modulus (n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;&nbsp;</div>{n} <br><br>
        """,
        unsafe_allow_html=True,
    )

    st.write('Nah kalau udah dicatet, [klik disini buat lanjut enkripsi & dekripsi imagenya ya!](encrypt_decrypt)\n')







