import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# FOOTER WATERMARK (ONLY)
# ----------------------------
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"]::after {
        content: "© Built by Saurabh Bhovad";
        position: fixed;
        bottom: 12px;
        right: 24px;
        font-size: 13px;
        color: rgba(255, 255, 255, 0.45);
        z-index: 9999;
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)



sns.set(style="whitegrid")

# ----------------------------
# Title Section
# ----------------------------
st.markdown(
    "<h1 style='text-align: center;'>📊 Student Performance Analysis Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Upload a CSV or Excel file to analyze student performance instantly</p>",
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# File Upload
# ----------------------------
uploaded_file = st.file_uploader(
    "📂 Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # ----------------------------
    # Data Preview
    # ----------------------------
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # ----------------------------
    # Basic Info
    # ----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 Dataset Shape")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

    with col2:
        st.subheader("⚠ Missing Values")
        st.write(df.isnull().sum())

    # ----------------------------
    # Feature Engineering
    # ----------------------------
    required_cols = {"math_score", "reading_score", "writing_score"}

    if required_cols.issubset(df.columns):

        df["total_score"] = (
            df["math_score"] +
            df["reading_score"] +
            df["writing_score"]
        )

        df["average_score"] = df["total_score"] / 3

        st.success("✅ Scores calculated successfully")

        # ----------------------------
        # Visual Analysis
        # ----------------------------
        st.subheader("📈 Visual Analysis")

        col3, col4 = st.columns(2)

        with col3:
            if "attendance" in df.columns:
                fig1 = plt.figure()
                sns.scatterplot(x="attendance", y="average_score", data=df)
                plt.title("Attendance vs Average Score")
                st.pyplot(fig1)

        with col4:
            if "study_hours" in df.columns:
                fig2 = plt.figure()
                sns.boxplot(x="study_hours", y="average_score", data=df)
                plt.title("Study Hours vs Performance")
                st.pyplot(fig2)

        if "gender" in df.columns:
            fig3 = plt.figure()
            sns.barplot(x="gender", y="average_score", data=df)
            plt.title("Average Score by Gender")
            st.pyplot(fig3)

        # ----------------------------
        # Correlation
        # ----------------------------
        st.subheader("📊 Correlation Heatmap")

        fig4 = plt.figure(figsize=(8, 5))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        st.pyplot(fig4)

        # ----------------------------
        # At-Risk Students
        # ----------------------------
        st.subheader("🚨 At-Risk Students (Avg Score < 50)")

        at_risk = df[df["average_score"] < 50]

        if at_risk.empty:
            st.info("No at-risk students found")
        else:
            st.dataframe(at_risk)

    else:
        st.error(
            "Dataset must contain math_score, reading_score, and writing_score columns"
        )

else:
    st.info("👆 Upload a CSV or Excel file to start analysis")
