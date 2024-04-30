# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM category;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.categoryid} has a :{row.categoryname}:")