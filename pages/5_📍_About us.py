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


st.set_page_config(page_title = "About us", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | SafeSpeak </h1>", unsafe_allow_html=True)



st.markdown("""
    <h1 style='font-size: 50px;'>About us📍</h1>
""", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="font-size: 20px;">
    SafeSpeak's mission is to empower safe online communication by detecting and mitigating cyberbullying. We are committed to creating a safer internet where everyone can communicate without fear of harassment.
    <br><br>
    Developed by a dedicated team of professionals, SafeSpeak leverages advanced machine learning and natural language processing (NLP) techniques to identify cyberbullying in real-time.
    <br><br>
    We are always looking for feedback and ways to improve. Reach out to us at <a href="mailto:info@safespeak.com">info@safespeak.com</a>.
    <br><br>
    <span style="font-size: 20px;">Stay updated with our latest developments and research</span>
</div>
""", unsafe_allow_html=True)

# Social Media Icons
st.markdown("""
    <div style="display: flex; justify-content: center; gap: 10px; margin-top: 10px;">
        <a href="https://twitter.com/safespeak" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/twitter.png" style="width:35px;height:35px;">
        </a>
        <a href="https://www.linkedin.com/company/safespeak" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/linkedin.png" style="width:35px;height:35px;">
        </a>
        <a href="https://www.facebook.com/safespeak" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/facebook.png" style="width:35px;height:35px;">
        </a>
    </div>
""", unsafe_allow_html=True)