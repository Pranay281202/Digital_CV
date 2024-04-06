from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit as st


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Pranay-Resume.pdf"
profile_pic = current_dir / "assets" / "My_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pranay Dilip Salkar"
PAGE_ICON = "📋"
NAME = "Pranay Dilip Salkar"
DESCRIPTION = """
As a recent graduate in Data Science, my goal is to dive into the corporate world to put my knowledge into action and grow as a professional.
I'm passionate about data science and eager to get practical experience. I want to use my skills to help organizations succeed.
"""

PROJECTS = {
"🏆 Car Price Predictor- Perfect prdiction on Car prices": "https://pranay281202-car-price-predictor-app-oduaky.streamlit.app/",
"🏆 HR Analytics using Power BI - Detailed analysis on specific HR Problem": "https://github.com/Pranay281202/HR-Analysis-using-PowerBI/blob/main/HR%20Analytics.pbix",
"🏆 Credit Score Classification - prediction of Credit Score using Machine Learning model": "https://github.com/Pranay281202/Credit-Score-Classification/blob/main/Credit%20score%20classification%20project.ipynb",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("\n")
    st.image(profile_pic, width=320)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # For Resume pdf Download
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")

st.write("- ✔️ BSc Data Science | KES Shroff College")
st.write("- - "+"2020 - 2023")
st.write("- ✔️ HSC | Sathaye College (Science)")
st.write("- - "+"2018 - 2020")
st.write("- ✔️ SSC | Marol Education Academy")
st.write("- - "+"2017 - 2018")

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
col1,col2 = st.columns(2)
with col1:
    st.write(
        """
    - ➡️ Python
    - ➡️ SQL
    - ➡️ Machine Learning
    - ➡️ Power BI/Tableau
    - ➡️ NLP
    """
    )
with col2:
    st.write(
        """
        - ➡️ Data Analysis
        - ➡️ Data Visualization
        - ➡️ Business acumen
        - ➡️ Problem-solving
        """
    )

# --- WORK HISTORY ---
st.write('\n') 
st.subheader("Work Experience")
st.write("---")
st.write("💻 [Machine Learning Intern by **Bharat Intern**](https://drive.google.com/file/d/19tqgShvHQhq19GtaU9I0u3sa0bzWySgn/view?usp=drive_link)")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Certificates ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write("⭐ [SQL Basic by Great learning](https://www.linkedin.com/posts/pranay-dilip-salkar_1000-free-courses-with-free-certificates-activity-7080074138630897665-4Sul?utm_source=share&utm_medium=member_desktop)")
st.write("⭐ [Advanced MS – Excel By KES Shroff College](https://drive.google.com/file/d/1Qsd7ftgDbqns-CN0_Kkga7Dtxzxtdw4V/view?usp=sharing)")
st.write("⭐ [Recommender System By KES Shroff College](https://drive.google.com/file/d/1Kv2hYn9hG6-w2aZBciz3RIZnJlzSDIaN/view?usp=drive_link)")
st.write('')

# Create columns for each social media link
col1, col2, col3, col4 = st.columns(4)
# Add LinkedIn link
# Add LinkedIn link
with col1:
    st.markdown('<a href="https://www.linkedin.com/in/pranay-dilip-salkar" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add GitHub link
with col2:
    st.markdown('<a href="https://github.com/Pranay281202" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)

# Add WhatsApp link
with col3:
    st.markdown('<a href="https://wa.me/9833282741?text=Hello%20there,%20thanks%20for%20connecting!" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1200px-WhatsApp.svg.png" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">WhatsApp</p>', unsafe_allow_html=True)

# Add Email link
with col4:
    st.markdown('<a href="mailto:salkarpranay2@gmail.com"  target="_blank" style="text-decoration:none;"><img src="https://workspace.google.com/static/img/products/png/gmail.png?cache=f50ecb6" alt="Email" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Email</p>', unsafe_allow_html=True)

# Add footer
st.write('---')
st.write('© Pranay Dilip Salkar  |  Last updated: April 2024')
