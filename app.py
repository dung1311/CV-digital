from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "final.pdf"
profile_pic = current_dir / "assets" / "round.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "DUNGNT CV"
PAGE_ICON = ":wave:"
NAME = "Nguyen Tien Dung"
DESCRIPTION = """
A highly motivated Computer Science student at HUST with a strong foundation in software development, data structures, and algorithms. I am eager to apply my technical skills in real-world projects, with a specific interest in computer vision and machine learning. My short-term goal is to gain hands-on experience in advanced research areas such as Optical Character Recognition (OCR), facial recognition, and object classification and detection. In the long term, I aspire to develop a deep expertise in computer vision, translating theoretical knowledge into impactful applications that drive innovation and address real-world challenges.
"""
EMAIL = "tiendung13112004@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/dung1311",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ALIGN CENTER IMAGE
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(profile_pic, width=230)
with col3:
    st.write(' ')
st.markdown(f"<h1 style='text-align: center; color: white;'>{NAME}</h1>", unsafe_allow_html=True)
# description
st.write(DESCRIPTION)
# align center download CV
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.download_button(
    label=" 📄 Download CV PDF",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
    )
with col3:
    st.write(' ')

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    
    # --- CONTACT ---
    st.header('CONTACT')
    st.write('---')
    st.write(':phone: 0869304580')
    st.write('📫 tiendung13112004@gmail.com')
    st.write(':house: Hong Mai, Hanoi')
    st.write(':link: https://github.com/dung1311')

    # --- EDUCATION ---
    st.header('EDUCATION')
    st.write('---')
    st.subheader("""
    2019 - 2022 \n
    Thai Nguyen For Gifted Student                     
    """)
    st.markdown('- Advanced mathematics class')
    st.subheader("""
    2022 - 2026 \n
    Hanoi University Of Science and Technology
    """)
    st.markdown('- Computer Science')
    st.markdown('- CPA: 3.44/4.0')

    # --- SKILLS --- 
    st.header('SKILLS')
    st.write('---')
    st.markdown('- Project Management')
    st.markdown('- Problem Solving')
    st.markdown('- Coding')
    st.markdown('- Data structure and Algorithm') 
    st.markdown('- OOP') 
    st.markdown('- Database') 
    st.markdown('- Python, Java, Javascript, C, C++') 
    st.markdown('- Pytorch, OpenCV, numpy, pandas, git') 

with col2:
    # --- PET PROJECTS ---
    st.header('PET PROJECTS')
    st.write('---')

    st.subheader('[Recognize Trash System](https://github.com/dung1311/HackScience23)')
    st.markdown('- Develop a waste classification and recognition system to support more effective environmental management.')
    st.markdown('- Processed and labeled image data related to various types of waste, Fine-tuned the model to improve accuracy and address challenges in classifying and recognizing complex waste types.')

    st.subheader('[News Aggregator](https://github.com/dung1311/OOP-Project-HUST)')
    st.markdown('- Developed a desktop application to automatically crawl and aggregate Bitcoin-related news from various websites.')
    st.markdown('- Led the project team as backend developer, overseeing integration and data management.')

    st.subheader('[Classfication Fashion-MNIST](https://github.com/dung1311/sofmaxt-regression)')
    st.markdown('- Build an image classification model to identify and categorize different types of clothing items using Softmax Regression. Achieved an accuracy of 86%.')

    st.subheader('[DATA4LIFE](https://github.com/dung1311/Data4Life)')
    st.markdown('- Processed extensive datasets and fine-tuned the YOLOv10 model for object detection tasks.')
    st.markdown('- Addressed a real-world problem by implementing a solution to count vehicles from aerial images.')

    st.subheader('[BKAI-CV-Projects](https://github.com/dung1311/BKAI-CV-Projects)')
    st.markdown('- Leveraging computer vision to tackle practical challenges such as object counting, image depth estimation, and scene analysis.')
    st.markdown('Continuously enhancing skills through hands-on problem-solving in computer vision.')

st.write('---')
