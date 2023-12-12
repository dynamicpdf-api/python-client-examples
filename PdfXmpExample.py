from dynamicpdf_api.pdf_xmp import PdfXmp
from dynamicpdf_api.pdf_resource import PdfResource
from Shared import *

def pdf_xmp_info(api_key, full_path):
    resource = PdfResource(full_path + "fw4.pdf")
    pdf_info = PdfXmp(resource)
    pdf_info.api_key = api_key
    response = pdf_info.process() 
    print(response.content)

if __name__ == "__main__":
    pdf_xmp_info(api_key, base_path + "/get-xmp-metadata-pdf-xmp-endpoint/")