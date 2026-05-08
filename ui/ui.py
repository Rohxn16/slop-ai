import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pov_generator.pov import POV
from pov_generator.generate import ChatPOVGenerator

# init objects
pov = POV()
chat_pov_generator = ChatPOVGenerator(model="llama3.2:3b", system_prompt=pov.SYSTEM_PROMPT_1)

st.write("# Welcome to Slop.AI !")
st.write('### Drop your story and generate your production ready video.')

story: str = st.text_area("Enter your story / context here. Do not exceed 2000 characters", height=400)
if st.button('Generate Script'):
    with st.spinner('Generating your POV story...'):
        pov_story = pov.generate_pov_from_text(story, chat_pov_generator)
    st.write("### Generated POV Story:")
    st.write(pov_story)
