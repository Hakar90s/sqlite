import streamlit as st
import sqlite3
from ui import show_table1_section, show_table2_section, show_table3_section
from pushpull import push_database

# Setup app
st.set_page_config(page_title="SQLite Streamlit App", layout="centered")
st.title("📊 Streamlit + SQLite (Auto GitHub Sync)")

# Connect to database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Table 1 (view + insert)
show_table1_section(cursor, conn)
push_database()

# Table 2 (view only)
show_table2_section(cursor)

# Table 3 (view + insert)
show_table3_section(cursor, conn)
push_database()

# Close DB connection
conn.close()
