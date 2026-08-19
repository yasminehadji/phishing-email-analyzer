import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "analyses.db"

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    with conn() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS analyses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        sender TEXT, subject TEXT, risk_score INTEGER, risk_level TEXT)""")
        c.commit()

def save_analysis(e, r):
    with conn() as c:
        c.execute("INSERT INTO analyses(sender,subject,risk_score,risk_level) VALUES(?,?,?,?)",
                  (e.get("sender",""), e.get("subject",""), r["score"], r["level"]))
        c.commit()

def get_recent_analyses(limit=20):
    with conn() as c:
        return c.execute("SELECT * FROM analyses ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
