import streamlit as st
import sqlite3

# Connect to SQLite DB in current directory
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

st.title("📋 My Online Streamlit + SQLite App")

# Show all data from table1
st.header("📂 Table 1 Records")
cursor.execute("SELECT * FROM table1")
data = cursor.fetchall()
st.dataframe(data)

# Add new entry
st.subheader("➕ Add New Record to Table 1")
with st.form("insert_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    status = st.selectbox("Status", ["Active", "Inactive"])
    material = st.text_input("Material")
    quantity = st.number_input("Quantity", min_value=0)
    price = st.number_input("Price", min_value=0.0)
    submitted = st.form_submit_button("Insert")

    if submitted:
        cursor.execute('''
            INSERT INTO table1 (name, age, status, material, quantity, price)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, age, status, material, quantity, price))
        conn.commit()
        st.success("✅ Record inserted successfully!")

conn.close()
