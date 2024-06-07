import streamlit as st
import time
import webbrowser as wb

st.title('Đăng nhập')
username = st.text_input('Username','')
password = st.text_input('Password','', type='password')
if st.button('Login'):
    if username == '21520255' and password == '2003':
        st.success('Đăng nhập thành công')
        time.sleep(3)
        wb.open('https://www.uit.edu.vn/')
    else:
        st.error('Sai username hoặc password')
#https://21520255-cau-2-2.streamlit.app/
