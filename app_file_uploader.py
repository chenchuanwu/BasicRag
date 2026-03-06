import os
from unittest import result
from dotenv import load_dotenv
import streamlit as st
import time
from knowledge_base import KnowledgeBaseService
load_dotenv()

st.title("Knowledge Base Uploader")

uploader_file=st.file_uploader(
    "Upload a file",
    type=["txt","pdf","docx","md"],
    accept_multiple_files=False)

#session_state is a dictionary
if "service" not in st.session_state:
    st.session_state["service"]= KnowledgeBaseService()


if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.subheader(f"File Information: {file_name}")
    st.write(f"File Type: {file_type}")
    st.write(f"File Size: {file_size:.2f} KB")

    st.write("File Content:")
    file_content = uploader_file.read()
    st.text_area("File Content", file_content, height=200)

   
    text = uploader_file.getvalue().decode("utf-8")
    st.write(text)
    with st.spinner("Uploading file..."):
        time.sleep(1)
        result=st.session_state["service"].upload_by_str(text,file_name)
        st.write(result)