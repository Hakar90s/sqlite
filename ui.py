import streamlit as st

def show_table1_section(cursor, conn):
    st.header("📋 Table 1 - Main Records")
    cursor.execute("SELECT * FROM table1")
    rows = cursor.fetchall()
    st.dataframe(rows)

    st.subheader("➕ Add Record to Table 1")
    with st.form("form_table1"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        status = st.selectbox("Status", ["Active", "Inactive"])
        material = st.text_input("Material")
        quantity = st.number_input("Quantity", min_value=0)
        price = st.number_input("Price", min_value=0.0)
        submitted = st.form_submit_button("Add to Table 1")

        if submitted:
            cursor.execute('''
                INSERT INTO table1 (name, age, status, material, quantity, price)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, age, status, material, quantity, price))
            conn.commit()
            st.success("✅ Added to table1 (triggered table2 insert)")

def show_table2_section(cursor):
    st.header("📑 Table 2 - Triggered Records")
    cursor.execute("SELECT * FROM table2")
    rows = cursor.fetchall()
    st.dataframe(rows)

def show_table3_section(cursor, conn):
    st.header("💰 Table 3 - Debts and Appointments")
    cursor.execute("SELECT * FROM table3")
    rows = cursor.fetchall()
    st.dataframe(rows)

    st.subheader("➕ Add Record to Table 3")
    with st.form("form_table3"):
        debt = st.number_input("Debt Amount", min_value=0.0)
        status = st.selectbox("Debt Status", ["Pending", "Paid"])
        appointment = st.date_input("Last Appointment Date")
        submitted = st.form_submit_button("Add to Table 3")

        if submitted:
            cursor.execute('''
                INSERT INTO table3 (debts, status, last_appointment)
                VALUES (?, ?, ?)
            ''', (debt, status, str(appointment)))
            conn.commit()
            st.success("✅ Added to table3")
