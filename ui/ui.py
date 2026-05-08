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

col1, col2 = st.columns([1, 4])
with col1:
    generate_clicked = st.button('Generate Script')
with col2:
    regenerate_clicked = False
    if 'pov_story' in st.session_state:
        regenerate_clicked = st.button('Regenerate Script')

if generate_clicked or regenerate_clicked:
    with st.spinner('Generating your POV story...'):
        st.session_state.pov_story = pov.generate_pov_from_text(story, chat_pov_generator)

if 'pov_story' in st.session_state:
    st.write("### Generated POV Story:")
    st.write(st.session_state.pov_story)
