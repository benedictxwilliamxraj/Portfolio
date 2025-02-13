import streamlit as st




if __name__=='__main__':
    st.set_page_config(layout="wide")

    st.sidebar.markdown('''
    # Portfolio
    - [About Me](#AboutMe)
    - [Skills](#skills)
    - [Work experience](#Workexperience)
    - [Projects](#projects)
    - [Achievements](#achievements)
    - [Contact Info](#contact)
    ''', unsafe_allow_html=True)

    # 1. About me
    st.header('About Me', divider=True)

    st.markdown("##### Hello,")
    st.subheader("I'm Benedict William Raj !!")
    st.markdown("###### Masters in Business Analytics '25 | BE CSE '21 | Data Engineering | AI/ML | Cloud Migration")
#     st.markdown("###### ")

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
            <p>Python,R, SQL, PHP, C, C++ </p>
        </li>
        <li><b>Database/Datawarehouse:</b>
            <p>Snowflake, PostgreSQL, MySQL, Oracle,Amazon S3</p>
        </li>
        <li><b>ETL & Data Integration Tools:</b>
            <p>Snowspark, ADF, Fivetran, Qlik, Airflow, Ascend.io, Databricks, Spark</p>
        </li>
        <li><b>Data Visualization:</b>
            <p>Streamlit, Matplotlib, Seaborn, Tableau, Excel</p>
        </li>
        <li><b>Machine Learning Frameworks/ Libraries: </b>
            <p>Darts, sklearn</p>
        </li>
    </ul>
    """, unsafe_allow_html=True)
    # 3. Work experience/ Services
    st.header('Work experience', divider=True)
    st.markdown("""
    <ul>
        <li><b> UNIVERSITY AT BUFFALO</b>
            <br>
            <i>Assistant</i>
            <ul>
                <li>Developed Python scripts to scrape and extract real-time data from websites, tailored to meet specific business requirements, ensuring accurate and relevant data collection for analysis.</li>
                <li>Applied linear programming to optimize resource allocation, balancing staffing needs against cost constraints.</li>
                <li>Developed a predictive forecasting model to estimate staffing needs under various growth scenarios.</li>
                <li>Built interactive dashboards using Streamlit to visualize staffing levels, resource utilization, and future projections, enabling dynamic data exploration for stakeholders.</li>
                <li>Delivered scenario analysis capabilities for predicting staffing needs under different growth projections.</li>
            </ul>
        </li>
        <hr>
        <li><b>GO DIGITAL TECHNOLOGY CONSULTING LLP </b>
            <br>
            <i>Data Engineer</i>
            <ul>
                <li>Collaborated with system architects, design analysts and project managers to understand business and industry needs.</li>
                <li>Designed and implemented data models tailored to fulfill the dynamic requirements of the business.</li>
                <li>Developed Oracle BI Publisher Report to perform ETL into Data Warehouse.</li>
                <li>Developed new data pipelines for Oracle Human Capital Management using Ascend and Snowflake to develop BI reports.</li>
                <li>Migrated Existing Oracle EBS modules to Fusion SCM modules (O2C, P2P, GLDM pipelines) into Snowflake.</li>
                <li>Optimized SQL queries for supply chain modules, resulting in faster execution of pipelines.</li>
                <li>Automated pipeline to extract and load of 100’s of table using Python.</li>
            </ul>
        </li>
        <hr>
        <li><b>LTIMINDTREE</b>
            <br>
            <i>Data Engineer</i>
            <ul>
                <li>Mentoring and leading a team of 2 junior data engineers to write concise, reusable, and scalable code.</li>
                <li>Collaborated on ETL (Extract, Transform, Load) tasks, maintaining data integrity, and verifying pipeline stability.</li>
                <li>Converted an existing Python/Pyspark ingestion pipeline to Snowpark and increased its performance by 80%.</li>
                <li>Designed and created new analytical dashboards using Tableau.</li>
                <li>Undertook cloud migration of traditional SQL system to Snowflake system.</li>
                <li>Learnt various ingestion tools Databricks, ADF, Fivetran and Qlik and built an ingestion pipeline.</li>
                <li>Created and optimized multiple time-efficient REST APIs with Python and Airflow for providing data to third party clients.</li>
                <li>Constructed a data lineage application to identify data origin and visibility for Snowflake.</li>
            </ul>
        </li>
        <hr>
        <li><b>TATA INSTITUTE OF FUNDAMENTAL RESEARCH</b>
            <br>
            <i> Research Intern</i>
            <ul>
                <li>Collaborated with research teams to develop project plans aligned with target timescales.</li>
                <li>Coded with PyQT5 and NodeJS to develop an AI Surveillance desktop application to monitor college CCTV.</li>
                <li>Trained YoloV4 model to detect humans and developed an email notification system to notify administrators.</li>
            </ul>
        </li>
        <hr>
        <li><b>KANALYTICS PRIVATE LIMITED</b>
            <br>
            <i>Data Science Intern</i>
            <ul>
                <li>Devised and trained new image search model to increase company productivity.</li>
                <li>Coded on Python and PHP to build end-to-end image recognition pipeline.</li>
            </ul>
        </li>
    </ul>
    """, unsafe_allow_html=True)
    # 4. Projects
    st.header('Projects', divider=True)
    st.markdown("""
    <ul>
        <li><b>HR RESOURCE FORECASTING</b>
            <br>
            <i><b>Tools:</b> Python, Streamlit </i>
            <p>
            Developed an end-to-end solution for workforce planning at a tax consultancy firm.
            Analyzed historical data to identify seasonal workload trends and employed a seasonal machine learning model, such as Prophet,
            to forecast workload for the next 52 days. Using these predictions, implemented linear programming to optimize employee allocation across departments, minimizing total staffing costs.
            Finally, designed an interactive dashboard to visualize forecasts, staffing requirements enabling data-driven decision-making for efficient resource management.
            <br>
            <i><a href="https://github.com/benedictxwilliamxraj/StaffForecasting">Github</a></i>
            </p>
        </li>
        <hr>
        <li><b>OLAP Integration Project</b>
            <br>
            <i><b>Tools</b> Snowflake, Ascend.io, SQL</i>
            <p>
            Migrated on-premise and Oracle Fusion data to a cloud-based architecture for improved efficiency and scalability.
            Extracted table data into CSV files and loaded them into the OCI staging area.
            Leveraged ASCEND.IO as the ETL tool to ingest data into Snowflake, where business transformations were performed using SQL. Designed and implemented dimension and fact tables, followed by creating visualization-ready tables.
            This setup enabled Power BI developers to directly utilize preprocessed data, minimizing processing power requirements within the Power BI application and enhancing performance.
            </p>
        </li>
        <hr>
        <li><b>Cloud migration</b>
            <br>
            <i><b>Tools: </b>Python, Snowpark</i>
            <p>
            Migrated an existing data processing pipeline from Spark with Pandas-based transformations to a Snowpark-compatible format,
            enabling seamless integration with Snowflake’s cloud ecosystem. Focused on optimizing the code to enhance efficiency, achieving an 80% improvement in processing time.
            This migration not only ensured cloud compatibility but also significantly boosted performance, making the data processing workflow more scalable and cost-effective within the cloud environment.
            </p>
        </li>
        <hr>
        <li><b>AISS</b>
            <br>
            <i><b>Tools:</b> Python, PyQT5, YoloV4</i>
            <p>
            Developed an AI-powered surveillance application for the college CCTV system (Hikvision) to improve video monitoring and security.
            The application integrated the Hikvision API to render live and recorded footage for real-time viewing.
            Additionally, I implemented an AI-based intruder detection system that identifies unauthorized movement in restricted areas and triggers alerts.
            In case of any intrusion, the system automatically sends an email with screenshots to the admin, enabling quick action.
            This project enhanced my skills in AI, CCTV system integration, and automation, providing a more efficient and secure solution for campus surveillance.
            <br>
            <i><a href="http://ijsart.com/Home/IssueDetail/47729">Publication</a></i>
            </p>
        </li>
        <hr>
        <li><b>Face Similarity Search</b>
            <br>
            <i><b>Tools: </b> Python, PHP</i>
            <p>
              Developed a face similarity search system using machine learning for facial recognition.
              Collected and trained a model on celebrity faces, storing their encodings in a JSON dictionary for efficient retrieval.
              The model was then integrated into an application to automatically detect and tag celebrities in images based on facial similarity.
              This project enhanced my expertise in computer vision, face recognition, and ML model deployment.
            </p>
        </li>
    </ul>
    """, unsafe_allow_html=True)
    # 4. Research Work and Publications
    # st.header('Research Work and Publications', divider=True)
    # 5. Achievements
    st.header('Achievements & Certifications', divider=True)
    st.markdown("""
    <ul>
        <li><a href="https://achieve.snowflake.com/3106f588-4301-4c78-a7d1-6094b43c2136#acc.uAkvTdYr">Snow Pro Certified: 2022-24, 2025-27</a></li>
        <li><a href="https://www.hackerrank.com/certificates/89a631c7ab94">SQL Basic Certified</a></li>
        <li><a href="https://www.hackerrank.com/certificates/abe8b960a9d7">SQL Medium Certified</a></li>
        <li>Programming Essentials In Python CISCO</li>
        <li>Won the Special Jury Award in Snowflake Hackathon 2021, organized by Snowflake, Aug 2021. </li>
        <li>Qualified to the Final Round in Smart India Hackathon 2020, organized by Govt of India, June 2020.</li>
    </ul>
    """, unsafe_allow_html=True)
    # 7. Contact Info
    st.header('Contact', divider=True)
    # 8. Get in touch with me
    st.markdown("""
    <h4>Email:</h4>
    <p>benedictwraj117@gmail.com</p>
    <h4>Phone</h4>
    <p>+1(716)-846-3192</p>
    """, unsafe_allow_html=True)


