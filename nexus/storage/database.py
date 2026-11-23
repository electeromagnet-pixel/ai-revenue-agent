"""Optional local SQLite store for raw source records."""
import sqlite3

def connect(path="nexus/data/nexus.sqlite3"):
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("""CREATE TABLE IF NOT EXISTS source_records (
        record_id TEXT PRIMARY KEY, source_url TEXT NOT NULL, source_title TEXT NOT NULL,
        collected_at TEXT NOT NULL, payload_json TEXT NOT NULL)""")
    connection.commit()
    return connection
