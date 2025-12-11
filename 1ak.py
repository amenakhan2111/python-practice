import streamlit as st
st.title("ATM note calculator")
amount=st.number_input("enter the amount")
if st.button("calculate"):
 five=0
 two=0
 one=0
if amount%100==0:
      if amount>=500:
           five=amount//500
           amount=amount-(five*500)
           st.success(f"500----{five}")
      if amount>=200:
            two=amount//200
            amount=amount-(two*200)
            st.success(f"200----{two}")
      if amount>=100:
            one=amount//100
            amount=amount-(one*100)
            st.success(f"100----{one}")
else:
       st.error("you have entered invalid amount")