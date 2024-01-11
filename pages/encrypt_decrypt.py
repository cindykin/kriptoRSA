import streamlit as st
import matplotlib.pyplot as plt
import zipfile
from style import style
from .util import RSA_encrypt, RSA_decrypt


st.set_page_config(
    page_title="Enkripsi gambar pake RSA Mini",
    page_icon="✨",
    layout="wide"
)

style()

col1, col2 = st.columns(2)

# Left column: Input
col1.header(":rainbow[Enkripsi]")

e = col1.number_input("Enter public key exponent (e)", min_value=0, step=1, value=0)
d = col1.number_input("Enter private key (d)", min_value=0, step=1, value=0)
n = col1.number_input("Enter modulus (n)", min_value=0, step=1, value=0)
user_file = col1.file_uploader("Choose an image file :sunglasses:", type=["jpg", "jpeg", "png"])

btn1 = col1.button('Enkripsi !')


    
encryption_completed = False
if btn1:
    cek_nilai = e != 0 and d != 0 and n != 0
    if user_file and cek_nilai:
        col1.write('Siap diterima.. tak proses dulu ya sebentar~')

        col1.write('Image Asli')
        col1.image(user_file, use_column_width=True)

        # Check the values of e, d, n
        col1.write(f'e={e}, d={d}, n={n}')

        encrypted_image, key_r_path, key_g_path, key_b_path = RSA_encrypt(user_file, e, n)

        # Display intermediate steps
        col1.image(encrypted_image[:, :, 0], caption="Encrypted Image (R)", use_column_width=True)
        col1.image(encrypted_image[:, :, 1], caption="Encrypted Image (G)", use_column_width=True)
        col1.image(encrypted_image[:, :, 2], caption="Encrypted Image (B)", use_column_width=True)

        col1.image(encrypted_image, caption="Encrypted Image", use_column_width=True)

        encrypted_image_path = 'encrypted_image.jpg'
        plt.imsave(encrypted_image_path, encrypted_image, format='jpg')

        decrypted_image = RSA_decrypt(encrypted_image, key_r_path, key_g_path, key_b_path, d, n)
        col1.image(decrypted_image, caption="Decrypted Image", use_column_width=True)

        decrypted_image_path = 'decrypted_image.jpg'
        plt.imsave(decrypted_image_path, decrypted_image, format='jpg')

        # Display intermediate steps
        col1.image(decrypted_image[:, :, 0], caption="Decrypted Image (R)", use_column_width=True)
        col1.image(decrypted_image[:, :, 1], caption="Decrypted Image (G)", use_column_width=True)
        col1.image(decrypted_image[:, :, 2], caption="Decrypted Image (B)", use_column_width=True)

        with zipfile.ZipFile('encrypted_data.zip', 'w') as zip_file:
            zip_file.write('encrypted_image.jpg')
            zip_file.write('decrypted_image.jpg')
            zip_file.write(key_r_path)
            zip_file.write(key_g_path)
            zip_file.write(key_b_path)

        encryption_completed = True
    else:
        st.write('Coba cek lagi, sudah masukkan gambar & mengetikkan e, d, n dengan benar belum?')

if encryption_completed:
      with open('encrypted_data.zip', 'rb') as zip_file:
          st.download_button(
              label="Download Data",
              data=zip_file,
              file_name='encrypted_data.zip',
              mime='application/zip',
          )

# Right column: Output
col2.header(":rainbow[Dekripsi]")

encryption_completed = False
if user_file and col2.button("Process"):
    st.session_state.button_clicked = True

    encrypted_image, key_r_path, key_g_path, key_b_path = RSA_encrypt(user_file, e, n)

    col2.image(encrypted_image, caption="Encrypted Image", use_column_width=True)

    encrypted_image_path = 'encrypted_image.jpg'
    plt.imsave(encrypted_image_path, encrypted_image, format='jpg')

    decrypted_image = RSA_decrypt(encrypted_image, key_r_path, key_g_path, key_b_path, d, n)
    col2.image(decrypted_image, caption="Decrypted Image", use_column_width=True)

    decrypted_image_path = 'decrypted_image.jpg'
    plt.imsave(decrypted_image_path, decrypted_image, format='jpg')

    with zipfile.ZipFile('encrypted_data.zip', 'w') as zip_file:
        zip_file.write('encrypted_image.jpg')
        zip_file.write('decrypted_image.jpg')
        zip_file.write(key_r_path)
        zip_file.write(key_g_path)
        zip_file.write(key_b_path)

    encryption_completed = True