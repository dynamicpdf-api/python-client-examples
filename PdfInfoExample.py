from dynamicpdf_api.pdf_info import PdfInfo
from dynamicpdf_api.pdf_resource import PdfResource
import pprint
import json
from Shared import *

def pdf_info_example(api_key, full_path):
    resource = PdfResource(full_path + "fw4.pdf")
    pdf_info = PdfInfo(resource)
    pdf_info.api_key = api_key
    response = pdf_info.process() 
    print(pprint.pformat(json.loads(response.json_content)))


if __name__ == "__main__":
    pdf_info_example(api_key, base_path + "/pdf-info/")