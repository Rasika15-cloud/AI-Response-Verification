# AI Response Verification Tool

## Project Overview
The AI Response Verification Tool is a Python-based application developed using Streamlit to evaluate AI-generated answers against expected answers.

It uses TF-IDF vectorization and cosine similarity to measure text similarity and determine whether an AI-generated answer meets the required similarity threshold.

## Features
- Compare expected answers with AI-generated answers
- Calculate text similarity scores using TF-IDF and Cosine Similarity
- PASS/FAIL results based on a configurable threshold
- Keyword coverage analysis
- Identify missing and additional keywords
- Detailed answer evaluation
- Dashboard with total tests, PASS, FAIL, and average score
- Store test results permanently using SQLite
- View previous test history
- Download verification reports in CSV format

## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- SQLite
- TF-IDF
- Cosine Similarity

## Project Structure

```text
AI_Response_Verification/
│
├── app.py
├── evaluation.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd AI_Response_Verification
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## How It Works

1. Enter a question.
2. Enter the expected answer.
3. Enter the AI-generated answer.
4. Set the minimum similarity threshold.
5. Click Verify Answer.
6. View the similarity score and PASS/FAIL status.
7. Review keyword coverage, missing information, and additional keywords.
8. View the results in the dashboard and download the report.

## Evaluation Method

- TF-IDF (Term Frequency–Inverse Document Frequency) is used to convert text into numerical features.
- Cosine similarity measures the similarity between the expected answer and the AI-generated answer.
- Keyword comparison calculates keyword coverage and identifies missing and additional words.

## Database

SQLite is used to store verification results locally, including questions, answers, scores, status, keyword coverage, and timestamps.

## Disclaimer

This tool uses text similarity and keyword-based evaluation. A high similarity score does not necessarily guarantee factual correctness or semantic equivalence. Results should be reviewed when accuracy is important.

## Author

Python | Automation | Software Testing | AI Project Development