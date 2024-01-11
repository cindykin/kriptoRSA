import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os
from style import style
from util import RSA_encrypt, RSA_decrypt

st.set_page_config(
    page_title="Enkripsi gambar pake RSA Mini",
    page_icon="🔐",
    layout="wide"
)

style()
col1, padding, col2 = st.columns((5,1,5))



col1.header(":rainbow[Enkripsi]")
col1.write('Yuk masukkan 3 nilai yang sudah kamu dpt dihalaman pertama tadi disini')

e = col1.number_input("Masukkan Public Key (e)", min_value=0, step=1, value=0)
d = col1.number_input("Masukkan Private Key (d)", key="key_private_e", min_value=0, step=1, value=0)
n = col1.number_input("Masukkan Modulus (n)", key="mod_e", min_value=0, step=1, value=0)
user_file = col1.file_uploader("Masukkin gambar ekstensi JPG only ya :sunglasses:", type=["jpg"])
btn1 = col1.button(':twisted_rightwards_arrows: Enkripsi !')




    
encrypt_completed = False

if btn1 :
    cek_nilai = e!=0 and d!=0 and n!= 0;
    if user_file and cek_nilai:
        col1.write('Siap diterima.. tak proses dulu ya 1-5 menit tergantung ukuran gambar~')

        col1.write('Gambar Asli :')
        col1.image(user_file, use_column_width=True)

        encrypted_image, encrypted_array, key_r_path, key_g_path, key_b_path = RSA_encrypt(user_file, e, n)

        col1.write(':tada:HASIL : BERHASIL TERENKRIPSI!!!:tada:')
        col1.write('Gambar yang sudah terenkripsi :')
        col1.image(encrypted_image, use_column_width=True)

        encrypted_image_path = 'encrypted_image.jpg'
        plt.imsave(encrypted_image_path, encrypted_image, format='jpg')

        with zipfile.ZipFile('encrypted_data.zip', 'w') as zip_file:
            zip_file.write('encrypted_image.jpg')
            zip_file.write(encrypted_array)
            zip_file.write(key_r_path)
            zip_file.write(key_g_path)
            zip_file.write(key_b_path)

        encrypt_completed = True
    else :
        st.write('coba cek lagi, sudah masukkan gambar & mengetikkan e,d,n dengan benar belum?')  

if encrypt_completed:
    with open('encrypted_data.zip', 'rb') as zip_file:
        st.download_button(
            label=":envelope_with_arrow: Download gambar yang sudah dienkripsi!",
            data=zip_file,
            file_name='encrypted_data.zip',
            mime='application/zip',
        )





col2.header(":rainbow[Dekripsi]")

col2.write('Sebelum mulai, ada dua cara nih kamu mau masukin gambar yang sudah dienkripsi dan key2nya atau file zip yang berisi semua file?')
col2.button('Sudah ')

xd = col2.number_input("Masukkan Private Key (d)", key="key_private_d", min_value=0, step=1, value=0)
xn = col2.number_input("Masukkan Modulus (n)", key="mod_d", min_value=0, step=1, value=0)
decrypt_file = col2.file_uploader("Masukkin file ZIP dari menu enkripsi tadi ya :sunglasses:", type=["zip"])

# Add a button to trigger decryption
btn_decrypt = col2.button(':twisted_rightwards_arrows: Dekripsi !')

decrypt_completed = False

# Check if the decryption button is clicked
if btn_decrypt and decrypt_file:
    # Extract the uploaded zip file
    with zipfile.ZipFile(decrypt_file, 'r') as zip_ref:
        zip_ref.extractall('decrypt_data')

    encrypted_image = 'decrypt_data/encrypted_image.jpg'
    encrypted_array = np.load('decrypt_data/encrypted_array.npy')
    key_r_path = 'decrypt_data/key_r.npy'
    key_g_path = 'decrypt_data/key_g.npy'
    key_b_path = 'decrypt_data/key_b.npy'
    
    decrypted_image = RSA_decrypt(encrypted_array, key_r_path, key_g_path, key_b_path, xd, xn)
    col2.image(decrypted_image, caption="Decrypted Image", use_column_width=True)
    decrypt_completed = True

if decrypt_completed:
    with open('decrypted_image.jpg', 'rb') as decrypted_file:
        st.download_button(
            label="Download Decrypted Image",
            data=decrypted_file,
            file_name='decrypted_image.jpg',
            mime='image/jpeg',  # Adjust the MIME type based on your file type
        )

if os.path.exists("decrypt_data"):
    os.rmdir("decrypt_data")