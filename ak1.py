import streamlit as st
st.title("welcome to streamlit")
username=st.text_input("enter username")
password=st.text_input("enter password")
if st.button("login"):
   if username=="admin":
      if password=="1234": 
         st.success("valid user")
      else:
         st.error("invalid password")
else:
   st.error("invalid error")