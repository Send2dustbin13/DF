import streamlit as st
import sqlite3
import pandas as pd


sqliteConnection = sqlite3.connect('test.db')
cursor = sqliteConnection.cursor()
print("Connected to SQLite")

sqlite_select_query = """SELECT * from emp"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()

df = df = pd.DataFrame(records)


block = st.container()

with st.expander("parameter"):
    st.write(df)
