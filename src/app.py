import streamlit as st
from services.blobservice import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Uploade de arquivo - Azure - Fake Docs")
    upload_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])


    if upload_file is not None:
        filename = upload_file.name
        #st.write(f"bytes {upload_file}" )
        blog_url = upload_blob(upload_file, filename)
        
        if blog_url is not None:
            st.write(f"Arquivo {filename} enviado com sucesso para Azure Blog Storage" )
            credit_card_info = analize_credit_card(blog_url)
            st.write(credit_card_info)
            show_image_validation(blog_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {filename} para Azure Blog Storage" )
        
            
def show_image_validation(blog_url, credit_card_info):
    st.image(blog_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação")

    if credit_card_info and credit_card_info["card_name"]:
        st.markdown("<h1 style='color: green'>Cartão validado</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Banco emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown("<h1 style='color: ref'>Cartão invalido</h1>", unsafe_allow_html=True)
        st.write(f"Este não é um cartão de credito validado")


    st.write(credit_card_info)





if __name__ == "__main__":
    configure_interface()


