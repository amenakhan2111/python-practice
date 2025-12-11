import streamlit as st
st.title("welcome to streamlit")
project=st.number_input("Enter project marks")     
internal=st.number_input("Enter internal marks")   
external=st.number_input("Enter external marks")
if st.button("calculate"):   
  if project>=50 and internal>=50 and external>=50:
    total=(project*70)/100+ (external*20)/100+(internal*10)/100
    st.write("Total score is: ",total)
    if total>=90:
        st.success("A grade")
    elif total>=70:
        st.success("B grade")
    else:
        st.success("C grade")