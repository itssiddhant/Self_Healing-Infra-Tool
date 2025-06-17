import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Self-Healing Infra Dashboard", layout="wide")

st.title("Self-Healing Infra Dashboard")

log_file = "actions.log"

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = f.readlines()
        df = pd.DataFrame({"Time & Action": logs})
        st.dataframe(df[::-1], use_container_width=True)
else:
    st.warning("No log file found.")

st.markdown("---")
st.info("This dashboard updates based on your 'actions.log' file.")
