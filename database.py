
import sqlite3
import pandas as pd

DB_NAME = "verification.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS verification_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            expected_answer TEXT,
            ai_answer TEXT,
            score REAL,
            status TEXT,
            keyword_coverage REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_result(question, expected_answer, ai_answer,
                score, status, keyword_coverage):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO verification_history
        (question, expected_answer, ai_answer,
         score, status, keyword_coverage)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        question,
        expected_answer,
        ai_answer,
        score,
        status,
        keyword_coverage
    ))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query("""
        SELECT
            id AS 'Test ID',
            question AS 'Question',
            expected_answer AS 'Expected Answer',
            ai_answer AS 'AI Answer',
            score AS 'Score',
            status AS 'Status',
            keyword_coverage AS 'Keyword Coverage',
            created_at AS 'Created At'
        FROM verification_history
        ORDER BY id DESC
    """, conn)

    conn.close()

    return df
