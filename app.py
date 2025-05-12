import streamlit as st
import sqlite3
from ui import show_table1_section, show_table2_section, show_table3_section
from pushpull import push_database

# Connect to SQLite
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Title
st.set_page_config(page_title="SQLite Streamlit App", layout="centered")
st.title("📊 Streamlit + SQLite App (Auto GitHub Sync)")

# Table 1: View + Add
show_table1_section(cursor, conn)
push_database()  # Push automatically after update

# Table 2: View only (triggered data)
show_table2_section(cursor)

# Table 3: View + Add
show_table3_section(cursor, conn)
push_database()

# Close connection
conn.close()
