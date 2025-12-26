📊 Student Performance Analysis Dashboard

A web-based data analysis dashboard that allows users to upload student performance data (CSV or Excel) and instantly visualize academic insights through interactive charts and tables.

This project focuses on exploratory data analysis (EDA) to understand how factors such as attendance and study hours impact student performance.


🚀 Features

Upload CSV or Excel files dynamically

Automatic data preview and validation

Feature engineering (total score & average score)

Interactive visualizations:

Attendance vs Performance

Study Hours vs Performance

Gender-wise Performance

Correlation Heatmap

Identification of at-risk students (average score < 50)

Clean and responsive UI built with Streamlit

Footer watermark for authorship identification


🛠️ Tech Stack

Python

Streamlit – UI & web app framework

Pandas – Data manipulation

Matplotlib & Seaborn – Data visualization

📂 Supported Dataset Format

The uploaded dataset should contain the following columns:

math_score

reading_score

writing_score

Optional but recommended columns:

attendance

study_hours

gender

The application automatically adapts based on available columns.

📈 Analysis Workflow

User uploads a dataset (CSV or Excel)

Data is validated and previewed

New features are created:

total_score

average_score

Visual exploratory analysis is performed

Correlation between numerical features is displayed

Students with low academic performance are highlighted

▶️ How to Run Locally
1. Clone the repository
git clone https://github.com/your-username/student-performance-analysis.git
cd student-performance-analysis

2. Install dependencies
pip install streamlit pandas matplotlib seaborn openpyxl

3. Run the application
streamlit run app.py


The app will open automatically in your browser at:

http://localhost:8501

📌 Use Cases

Academic performance analysis

Educational data exploration

Portfolio demonstration for Data Analyst / Data Science roles

Teaching basic EDA concepts

🔮 Future Enhancements

Add machine learning models for performance prediction

Downloadable analysis reports (PDF/CSV)

Custom column selection by users

Deployment on Streamlit Cloud

Authentication and role-based access

👤 Author

Saurabh Bhovad
MCA Student | Data Analytics & Data Science Enthusiast

This project is created for learning and portfolio purposes.

📜 License

This project is open for educational use.
Reproduction or redistribution without proper credit is discouraged.
