from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analize_credit_card(card_url):   
    try:

        crediantials =AzureKeyCredential(Config.DOC_API_KEY)
        document = DocumentIntelligenceClient(Config.DOC_CONNECTION_STRING, crediantials)   

        card_info = document.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url) )                  

        result = card_info.result()

        for document in result.documents:
            fields = document.get('fields', {})

            return {
                     "card_name": fields.get('CardHolderName', {}).get('content'),
                    "card_number": fields.get('CardNumber', {}).get('content'),
                    "expiry_date": fields.get('ExpirationDate', {}).get('content'),
                    "bank_name": fields.get('IssuingBank', {}).get('content'),
                }
    except Exception as ex:
        print (ex)
        return ex