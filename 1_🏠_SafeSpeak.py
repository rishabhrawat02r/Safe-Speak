import streamlit as st
from PIL import Image

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')
main_image = Image.open('icons/img1.png')


st.set_page_config(page_title = "SafeSpeak", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'> © 2024 | SafeSpeak </h1>", unsafe_allow_html=True)

# st.image(image , use_column_width=True)

col1, col2 = st.columns([4, 4])

with col1:
    st.markdown("""
        <h1 style="font-size: 60px; color: #0080FF; margin-top: 55px; margin-left: -150px;">SafeSpeak</h1>
        <h3 style="font-size: 30px; margin-bottom: 20px; margin-left: -150px;">Empowering Safe Online Communication</h3>
    """, unsafe_allow_html=True)

with col2:
    st.image(main_image, use_column_width=True, caption=None)

# Additional CSS for further customization
st.markdown("""
    <style>
    .css-1aumxhk { /* Class selector for the main content area */
        padding-top: 0; /* Remove the padding at the top */
    }
    </style>
    """, unsafe_allow_html=True)

