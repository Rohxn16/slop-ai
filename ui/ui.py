import streamlit as st
import os

st.write("# Welcome to Slop.AI !")
st.write('### Drop your story and generate your production ready video.')

story: str = st.text_area("Enter your story / context here. Do not exceed 2000 characters", height=400)
if st.button('Generate Script'):
    print(story)
