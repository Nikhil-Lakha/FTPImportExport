import streamlit as st
 
# App Title
st.title("Data Import and Export App")
 
# Create two tabs
tab1, tab2 = st.tabs(["Import", "Export"])
 
# --- Import Tab ---
with tab1:
    st.header("Import Data")
 
    st.subheader("FTP Credentials for Import")
    import_host = st.text_input("Hostname (Import)", key="import_host")
    import_user = st.text_input("Username (Import)", key="import_user")
    import_pass = st.text_input("Password (Import)", type="password", key="import_pass")
 
    # Optional: Show entered values (for dev only, remove in production)
    # st.write(f"Host: {import_host}, User: {import_user}, Password: {import_pass}")
 
# --- Export Tab ---
with tab2:
    st.header("Export Data")
 
    st.subheader("FTP Credentials for Export")
    export_host = st.text_input("Hostname (Export)", key="export_host")
    export_user = st.text_input("Username (Export)", key="export_user")
    export_pass = st.text_input("Password (Export)", type="password", key="export_pass")
 
    # Optional: Show entered values (for dev only, remove in production)
    # st.write(f"Host: {export_host}, User: {export_user}, Password: {export_pass}")
