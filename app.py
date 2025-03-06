import streamlit as st
import streamlit_gsheets as gsheets
from streamlit.connections import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("AI Agent Survey")
st.markdown("Enter your feedback below:")

# Establishing a Google Sheets connection
# conn = st.experimental_connection("gsheets", type=GSheetsConnection)
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing data from Google Sheets (TEST)
existing_data = conn.read(worksheet="surveySheet", usecols=list(range(5), ttl=4))
existing_data = existing_data.dropna(how="all")

st.dataframe(existing_data)
