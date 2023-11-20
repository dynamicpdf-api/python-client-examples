from dynamicpdf_api.pdf_text import PdfText
from dynamicpdf_api.pdf_resource import PdfResource

def run(api_key):
    resource = PdfResource("C:/temp/dynamicpdf-api-samples/pdf-info/fw4.pdf")
    pdf_text = PdfText(resource)
    pdf_text.api_key = api_key
    pdf_text.start_page=1
    pdf_text.page_count=2
    response = pdf_text.process()
    print(response.json_content)

if __name__ == "__main__":
    api_key = "DP.xxx-api-key-xxx"
    run(api_key)