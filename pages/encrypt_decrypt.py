import streamlit as st
import matplotlib.pyplot as plt
import zipfile
import os
import shutil
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




    
encrypt_completed = False

if col1.button(':twisted_rightwards_arrows: Enkripsi !') :
    cek_nilai = e!=0 and d!=0 and n!= 0;
    if user_file and cek_nilai:
        col1.write('Siap diterima.. tak proses dulu ya 1-5 menit tergantung ukuran gambar~')

        col1.write(':blue[***Gambar Asli :***]')
        col1.image(user_file, use_column_width=True)

        encrypted_image, encrypted_array, key_r_path, key_g_path, key_b_path = RSA_encrypt(user_file, e, n)

        col1.divider()
        col1.write(':tada: **HASIL : BERHASIL DIENKRIPSI!!!** :tada:')
        col1.write(':blue[***Gambar yang sudah terenkripsi :***]')
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
        col1.write('coba cek lagi, sudah masukkan gambar & mengetikkan e,d,n dengan benar belum?')  

if encrypt_completed:
    with open('encrypted_data.zip', 'rb') as zip_file:
        done = col1.download_button(
            label=":envelope_with_arrow: Download gambar yang sudah dienkripsi!",
            data=zip_file,
            file_name='encrypted_data.zip',
            mime='application/zip',
        )

    if done :
        os.remove('./encrypted_array.npy')
        os.remove('./key_r.npy')
        os.remove('./key_g.npy')
        os.remove('./key_b.npy')





col2.header(":rainbow[Dekripsi]")

col2.write('Sebelum mulai, ada dua cara nih kamu mau masukin gambar yang terenkripsi dan key2nya atau file zip yang berisi semua file?')

option = col2.radio(
    "Pilih salah satu ya",
    [":blue[Upload file satu-satu]", ":blue[Upload ZIP]"],
    captions = ["1 per 1 cape sih, mending zip", "paling ez tinggal upload", "Never stop learning."],
    index=None
)
col2.divider()
decrypt_completed = False

if option == ":blue[Upload file satu-satu]":
    col2.subheader('_Dekripsi dari masing2 file_')
    xd = col2.number_input("Masukkan Private Key (d)", key="key_private_d", min_value=0, step=1, value=0)
    xn = col2.number_input("Masukkan Modulus (n)", key="mod_d", min_value=0, step=1, value=0)
    
    encrypted_array = col2.file_uploader("Masukkin file encrypted_array dari menu enkripsi tadi ya :sunglasses:", type=["npy"])
    key_r_path = col2.file_uploader("Masukkin file key r", type=["npy"])
    key_g_path = col2.file_uploader("Masukkin file key g", type=["npy"])
    key_b_path = col2.file_uploader("Masukkin file key b", type=["npy"])

    if col2.button(":twisted_rightwards_arrows: Dekripsi !", key='decrypt1') :
        if xd != 0 and xn != 0 and encrypted_array:
            col2.write('Siap diterima.. tak proses dulu ya 1-5 menit tergantung ukuran gambar~')

            decrypted_image = RSA_decrypt(encrypted_array, key_r_path, key_g_path, key_b_path, xd, xn)
        
            col2.write(':tada: **HASIL : BERHASIL DIDEKRIPSI!!!** :tada:')
            col2.write(':blue[***Gambar yang sudah terdekripsi :***]')
            col2.image(decrypted_image, use_column_width=True)

            decrypted_image_path = 'decrypted_image.jpg'
            plt.imsave(decrypted_image_path, decrypted_image, format='jpg')

            decrypt_completed = True
        else:
            col2.write('coba cek lagi, sudah masukkan semua file & mengetikkan d,n dengan benar belum?')

elif option == ":blue[Upload ZIP]":
    col2.subheader('_Dekripsi dari ZIP_')
    xd = col2.number_input("Masukkan Private Key (d)", key="key_private_d", min_value=0, step=1, value=0)
    xn = col2.number_input("Masukkan Modulus (n)", key="mod_d", min_value=0, step=1, value=0)
    decrypt_file = col2.file_uploader("Masukkin file ZIP dari menu enkripsi tadi ya :sunglasses:", type=["zip"])



    if col2.button(":twisted_rightwards_arrows: Dekripsi !", key='decrypt2') :
        if xd != 0 and xn != 0 and decrypt_file:
            col2.write('Siap diterima.. tak proses dulu ya 1-5 menit tergantung ukuran gambar~')

            with zipfile.ZipFile(decrypt_file, 'r') as zip_ref:
                zip_ref.extractall('decrypt_data')

                encrypted_array = 'decrypt_data/encrypted_array.npy'
                key_r_path = 'decrypt_data/key_r.npy'
                key_g_path = 'decrypt_data/key_g.npy'
                key_b_path = 'decrypt_data/key_b.npy'

            decrypted_image = RSA_decrypt(encrypted_array, key_r_path, key_g_path, key_b_path, xd, xn)
            col2.write(':tada: **HASIL : BERHASIL DIDEKRIPSI!!!** :tada:')
            col2.write(':blue[***Gambar yang sudah terdekripsi :***]')
            col2.image(decrypted_image, use_column_width=True)

            decrypted_image_path = 'decrypted_image.jpg'
            plt.imsave(decrypted_image_path, decrypted_image, format='jpg')

            decrypt_completed = True
        else:
            col2.write('coba cek lagi, sudah upload file zip & mengetikkan d,n dengan benar belum?')




if decrypt_completed:
    with open('decrypted_image.jpg', 'rb') as decrypted_image:
        done = col2.download_button(
            label="Download Decrypted Image",
            data=decrypted_image,
            file_name='decrypted_image.jpg',
            mime='image/jpg',  
        )

    if done :
        if os.path.exists("decrypt_data"):
            shutil.rmtree("decrypt_data")

