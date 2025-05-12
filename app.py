import streamlit as st
import sqlite3
import pushpull  # This is your GitHub sync module

# --- Sidebar GitHub Sync Buttons ---
st.sidebar.header("🔁 GitHub Sync")
if st.sidebar.button("⬇️ Pull DB from GitHub"):
    pushpull.pull_database()

if st.sidebar.button("⬆️ Push DB to GitHub"):
    pushpull.push_database()

# --- Database Connection ---
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

st.title("📊 Streamlit App with SQLite (3 Tables)")

# -------------------------------
# 📋 Table 1 - Main Records
# -------------------------------
st.header("📋 Table 1 - Main Records")
cursor.execute("SELECT * FROM table1")
rows1 = cursor.fetchall()
st.dataframe(rows1)

# Insert into Table 1
st.subheader("➕ Add Record to Table 1")
with st.form("form_table1"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    status = st.selectbox("Status", ["Active", "Inactive"])
    material = st.text_input("Material")
    quantity = st.number_input("Quantity", min_value=0)
    price = st.number_input("Price", min_value=0.0)
    submit1 = st.form_submit_button("Add to Table 1")
    if submit1:
        cursor.execute('''
            INSERT INTO table1 (name, age, status, material, quantity, price)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, age, status, material, quantity, price))
        conn.commit()
        st.success("✅ Added to table1 (and triggered insert to table2)")

# -------------------------------
# 📑 Table 2 - Triggered Data
# -------------------------------
st.header("📑 Table 2 - Triggered Data from Trigger")
cursor.execute("SELECT * FROM table2")
rows2 = cursor.fetchall()
st.dataframe(rows2)

# -------------------------------
# 💰 Table 3 - Debts & Appointments
# -------------------------------
st.header("💰 Table 3 - Debts and Appointments")
cursor.execute("SELECT * FROM table3")
rows3 = cursor.fetchall()
st.dataframe(rows3)

st.subheader("➕ Add Record to Table 3")
with st.form("form_table3"):
    debt = st.number_input("Debt Amount", min_value=0.0)
    status3 = st.selectbox("Debt Status", ["Pending", "Paid"])
    appointment = st.date_input("Last Appointment Date")
    submit3 = st.form_submit_button("Add to Table 3")
    if submit3:
        cursor.execute('''
            INSERT INTO table3 (debts, status, last_appointment)
            VALUES (?, ?, ?)
        ''', (debt, status3, str(appointment)))
        conn.commit()
        st.success("✅ Record added to table3")

# --- Close database connection ---
conn.close()
