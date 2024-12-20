import streamlit as st




if __name__=='__main__':
    st.set_page_config(layout="wide")

    st.sidebar.markdown('''
    # Portfolio
    - [About Me](#aboutme)
    - [Skills ](#skills)
    - [Projects](#projects)
    - [Research Work and Publications](#r&p)
    - [Achievements](#Achievements)
    - [Work experience](#services)
    - [Contact Info](#contact)
    ''', unsafe_allow_html=True)

    # 1. About me
    st.header('About Me', divider=True)
    st.markdown("##### Hello,")
    st.subheader("I'm Benedict William Raj !!")
    st.markdown("###### Masters in Business Analytics '25 | BE CSE '21 | Data Engineering | AI/ML | Cloud Migration")
    st.markdown("###### ")

    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(
            """
            <div style="background-color: #FFFFFF; padding: 10px; border-radius: 5px; width: 100%; margin: 0 auto;">
                <p style="color: #34495E;">I am a skilled data professional currently pursuing Masters in <b>Business Analytics at the University at Buffalo</b>, with an expected graduation date of June 2025. Holding a Bachelor of Engineering in <b>Computer Engineering</b> from the University of Mumbai, I bring a strong foundation in both technical and analytical problem-solving.
                I am passionate about leveraging data to drive business insights and innovation, and I am eager to contribute to impactful projects in <b>Data Analytics, Data Science, Machine Learning,Computer Vision and Natural Language Processing</b>.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        pdf_path = "BenedictResume122024.pdf"
        with open(pdf_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        st.write("")
        st.download_button(
            label="Download Resume",
            data=pdf_data,
            file_name="BenedictResume122024.pdf",
            mime="application/pdf",
        )
    with col2:
        st.image("benedict.jpeg", use_container_width=False, width=380)

    # 2. Skills
    st.header('Skills', divider=True)
    st.markdown("""
    <ul>
        <li><b>Languages:</b>
            <p>Python, SQL, PHP, C, C++ </p>
        </li>
        <li><b>Database/Datawarehouse:</b>
            <p>Snowflake, PostgreSQL, MySQL, Oracle,Amazon S3, Spark</p>
        </li>
        <li><b>ETL & Data Integration Tools:</b>
            <p>ADF, Fivetran, Qlik, Airflow, Ascend.io, Databricks</p>
        </li>
        <li><b></b>
            <p></p>
        </li>
    </ul>
    """, unsafe_allow_html=True)
    # 3. Projects
    st.header('Projects', divider=True)
    # 4. Research Work and Publications
    st.header('Research Work and Publications', divider=True)
    # 5. Achievements
    st.header('Achievements', divider=True)
    # 6. Work experience/ Services
    st.header('Work experience', divider=True)
    # 7. Contact Info
    st.header('Contact', divider=True)
    # 8. Get in touch with me


