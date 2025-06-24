import streamlit as st
from ftplib import FTP
from io import BytesIO
 
st.title("Data Import and Export App")
 
tab1, tab2 = st.tabs(["Import", "Export"])
 
# ---------- IMPORT TAB ----------
with tab1:
    st.header("Import Data")
 
    st.subheader("FTP Credentials for Import")
    import_host = st.text_input("Hostname (Import)", key="import_host")
    import_user = st.text_input("Username (Import)", key="import_user")
    import_pass = st.text_input("Password (Import)", type="password", key="import_pass")
 
    if import_host and import_user and import_pass:
        try:
            ftp = FTP(import_host)
            ftp.login(import_user, import_pass)
            st.success("Connected to FTP successfully.")
 
            uploaded_file = st.file_uploader("Choose a file to upload to FTP", key="upload")
            if uploaded_file is not None:
                file_name = uploaded_file.name
                        file_content = uploaded_file.read()
                        bio = BytesIO(file_content)
         
                        if st.button("Upload File"):
                            ftp.storbinary(f"STOR {file_name}", bio)
                            st.success(f"File '{file_name}' uploaded successfully.")
                            ftp.quit()
                except Exception as e:
                    st.error(f"FTP connection failed: {e}")
 
# ---------- EXPORT TAB ----------
with tab2:
    st.header("Export Data")
 
    st.subheader("FTP Credentials for Export")
    export_host = st.text_input("Hostname (Export)", key="export_host")
    export_user = st.text_input("Username (Export)", key="export_user")
    export_pass = st.text_input("Password (Export)", type="password", key="export_pass")
 
    if export_host and export_user and export_pass:
        try:
            ftp = FTP(export_host)
            ftp.login(export_user, export_pass)
            st.success("Connected to FTP successfully.")
 
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
                ftp.quit()
            else:
st.info("No files found on FTP server.")
        except Exception as e:
            st.error(f"FTP connection failed: {e}")
