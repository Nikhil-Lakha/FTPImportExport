import streamlit as st
 
# App Title
st.title("Data Import and Export App")
 
# Create two tabs
tab1, tab2 = st.tabs(["Import", "Export"])
 
# Content for the Import tab
with tab1:
    st.header("Import")
    st.write("Upload your file or connect to a data source.")
 
# Content for the Export tab
with tab2:
    st.header("Export")
    st.write("Download or export your transformed data.")
