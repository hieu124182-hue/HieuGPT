import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trends (
    keyword TEXT,
    score INTEGER
)
""")


def save_trends(trends):
    for word, score in trends:
        cursor.execute(
            "INSERT INTO trends (keyword, score) VALUES (?, ?)",
            (word, score)
        )

    conn.commit()
