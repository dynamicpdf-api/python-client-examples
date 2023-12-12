from dynamicpdf_api.pdf_text import PdfText
from dynamicpdf_api.pdf_resource import PdfResource
from Shared import *

def pdf_text_example(apikey, full_path):
    resource = PdfResource(full_path + "fw4.pdf")
    pdf_text = PdfText(resource)
    pdf_text.api_key = apikey
    pdf_text.start_page=1
    pdf_text.page_count=2
    response = pdf_text.process()
    print(response.json_content)

if __name__ == "__main__":
    pdf_text_example(api_key, base_path + "/pdf-info/")