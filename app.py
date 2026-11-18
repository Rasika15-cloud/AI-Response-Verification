
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from evaluation import evaluate_answer
from database import create_table, save_result, get_history


st.set_page_config(
    page_title="AI Response Verification",
    page_icon="🤖"
)

create_table()

df = get_history()

st.title("🤖 AI Response Verification Tool")

st.write("Evaluate AI-generated answers using text similarity.")



# User inputs
question = st.text_input("Enter your question")

expected_answer = st.text_area("Enter expected answer")

ai_answer = st.text_area("Enter AI-generated answer")

threshold = st.slider(
    "Minimum similarity score for PASS (%)",
    min_value=0,
    max_value=100,
    value=50
)

# Verify button
if st.button("Verify Answer"):

    if not question.strip():
        st.warning("Please enter a question.")

    elif not expected_answer.strip() or not ai_answer.strip():
        st.warning("Please enter both answers.")

    else:
        try:
            # Calculate similarity
            vectorizer = TfidfVectorizer()

            vectors = vectorizer.fit_transform(
                [expected_answer, ai_answer]
            )

            score = cosine_similarity(
                vectors[0:1],
                vectors[1:2]
            )[0][0]

            percentage = round(score * 100, 2)

            if percentage >= threshold:
                status = "PASS"
                st.success("PASS - Answers are similar")
            else:
                status = "FAIL"
                st.error("FAIL - Answers are different")

            st.metric("Similarity Score", f"{percentage}%")

            # Detailed evaluation
            evaluation = evaluate_answer(
                question,
                expected_answer,
                ai_answer
            )

            st.subheader("Detailed Evaluation")

            st.write("Relevance:", evaluation["relevance"])
            st.write("Completeness:", evaluation["completeness"])

            st.metric(
                "Keyword Coverage",
                f'{evaluation["keyword_coverage"]}%'
            )

            st.write(
                "Missing Information:",
                evaluation["missing_information"]
            )

            st.write(
                "Additional Keywords:",
                evaluation["extra_keywords"]
            )

            save_result(
                question,
                expected_answer,
                ai_answer,
                percentage,
                status,
                evaluation["keyword_coverage"]
            )

            st.success("Result saved permanently in database!")

        except ValueError:
            st.warning(
                "Unable to compare these answers. "
                "Please enter meaningful text."
            )

# Evaluation Dashboard
st.subheader("📈 Evaluation Dashboard")

df = get_history()

if not df.empty:

    total_tests = len(df)

    pass_count = (df["Status"] == "PASS").sum()
    fail_count = (df["Status"] == "FAIL").sum()

    average_score = round(df["Score"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Tests", total_tests)
    col2.metric("PASS", pass_count)
    col3.metric("FAIL", fail_count)
    col4.metric("Average Score", f"{average_score}%")

    st.subheader("Test Result Summary")

    chart_data = pd.DataFrame({
        "Result": ["PASS", "FAIL"],
        "Count": [pass_count, fail_count]
    })

    st.bar_chart(
        chart_data.set_index("Result")
    )

    # Permanent Test History
    st.subheader("📊 Test History")

    st.dataframe(df, use_container_width=True)

    # Download CSV
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Verification Report",
        data=csv,
        file_name="AI_Verification_Report.csv",
        mime="text/csv",
        key="sqlite_download_report"
    )

else:

    st.info("No test results available yet.")

