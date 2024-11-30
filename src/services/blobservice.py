import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config

def upload_blob(file, filename):
    try:    
        if not Config.STORAGE_CONNECTION_STRING:
            st.error("A string de conexão do Azure Blob não está configurada.")
            return None
        
        if file is None:
            st.error("Nenhum arquivo foi selecionado para upload.")
            return None
        
        file_bytes = file.read() 

        blob_service_client = BlobServiceClient.from_connection_string(Config.STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(file_bytes, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para Azure Blob: {ex}")
        return None
