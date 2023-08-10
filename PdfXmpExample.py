from dynamicpdf_api.pdf_xmp import PdfXmp
from dynamicpdf_api.pdf_resource import PdfResource

def run(api_key):
    resource = PdfResource("C:/temp/dynamicpdf-api-samples/pdf-info/fw4.pdf")
    pdf_info = PdfXmp(resource)
    pdf_info.api_key = api_key
    response = pdf_info.process() 
    print(response.content)

if __name__ == "__main__":
    api_key = "DP---API-KEY---"
    run(api_key)