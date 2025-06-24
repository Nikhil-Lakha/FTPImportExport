import streamlit as st
from ftplib import FTP
from io import BytesIO
 
# Initialize FTP profiles dict in session state
if "ftp_profiles" not in st.session_state:
    st.session_state.ftp_profiles = {}
 
st.title("Data Import and Export App")
 
tab1, tab2 = st.tabs(["Import", "Export"])
 
# --------- Helper Function ---------
def connect_ftp(host, user, password):
    ftp = FTP(host)
    ftp.login(user, password)
    return ftp
 
# --------- IMPORT TAB ---------
with tab1:
    st.header("Import Data")
 
    st.subheader("FTP Credentials for Import")
    import_profile_name = st.text_input("Save this connection as (Import)", key="import_profile_name")
    import_host = st.text_input("Hostname (Import)", key="import_host")
    import_user = st.text_input("Username (Import)", key="import_user")
    import_pass = st.text_input("Password (Import)", type="password", key="import_pass")
 
    if import_host and import_user and import_pass:
        try:
            ftp = connect_ftp(import_host, import_user, import_pass)
            st.success("Connected to FTP successfully.")
 
            # Save profile if a name is given
            if import_profile_name:
                st.session_state.ftp_profiles[import_profile_name] = {
                    "host": import_host,
                    "user": import_user,
                    "pass": import_pass
                }
                st.success(f"Connection saved as '{import_profile_name}'")
 
            uploaded_file = st.file_uploader("Choose a file to upload to FTP", key="upload")
            if uploaded_file:
                file_name = uploaded_file.name
                file_content = uploaded_file.read()
                bio = BytesIO(file_content)
 
                if st.button("Upload File"):
                    ftp.storbinary(f"STOR {file_name}", bio)
                    st.success(f"File '{file_name}' uploaded successfully.")
            ftp.quit()
        except Exception as e:
            st.error(f"FTP connection failed: {e}")
 
# --------- EXPORT TAB ---------
with tab2:
    st.header("Export Data")
 
    st.subheader("FTP Credentials for Export")
    export_profile_name = st.text_input("Save this connection as (Export)", key="export_profile_name")
    export_host = st.text_input("Hostname (Export)", key="export_host")
    export_user = st.text_input("Username (Export)", key="export_user")
    export_pass = st.text_input("Password (Export)", type="password", key="export_pass")
 
    if export_host and export_user and export_pass:
        try:
            ftp = connect_ftp(export_host, export_user, export_pass)
            st.success("Connected to FTP successfully.")
 
            # Save profile if a name is given
            if export_profile_name:
                st.session_state.ftp_profiles[export_profile_name] = {
                    "host": export_host,
                    "user": export_user,
                    "pass": export_pass
                }
                st.success(f"Connection saved as '{export_profile_name}'")
 
            files = ftp.nlst()
            if files:
                st.write("Files available for download:")
                for file in files:
                    if st.button(f"Download {file}", key=f"dl_{file}"):
                        buffer = BytesIO()
                        ftp.retrbinary(f"RETR {file}", buffer.write)
                        buffer.seek(0)
                        st.download_button(label=f"Click to download {file}",
                                           data=buffer,
                                           file_name=file)
            else:
                st.info("No files found.")
                ftp.quit()
        except Exception as e:
            st.error(f"FTP connection failed: {e}")
 
# --------- Show Saved Profiles (Optional Debug/UX) ---------
with st.expander("📁 Saved FTP Profiles"):
    if st.session_state.ftp_profiles:
        for name, creds in st.session_state.ftp_profiles.items():
            st.write(f"**{name}** → Host: `{creds['host']}`, User: `{creds['user']}`")
    else:
        st.info("No saved profiles yet.")
