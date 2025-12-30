import streamlit as st
import snowflake.connector
from ai.sql_builder import build_sql
from ai.schema_introspector import get_tables

conn = snowflake.connector.connect(
    user=st.secrets["user"],
    password=st.secrets["password"],
    account=st.secrets["account"],
    warehouse=st.secrets["warehouse"],
    database="DEMO_DB",
    schema="L2_SCHEMA"
)

st.title("❄️ Gold Layer SQL Builder")

user_input = st.text_area("Describe your analytical table")

if st.button("Generate SQL"):
    tables = get_tables(conn, "L2_SCHEMA")
    sql = build_sql(user_input, tables)
    st.code(sql, language="sql")
