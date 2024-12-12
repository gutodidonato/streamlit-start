import streamlit as st

def show_metric(label, value, prefix=""):
    st.metric(label, f"{prefix}{value:,.2f}")
