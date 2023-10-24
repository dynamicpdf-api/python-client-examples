from dynamicpdf_api.pdf_info import PdfInfo
from dynamicpdf_api.pdf_resource import PdfResource
import pprint
import json

def run(api_key, basePath):
    resource = PdfResource(basePath + "fw9AcroForm_18.pdf")
    pdf_info = PdfInfo(resource)
    pdf_info.api_key = api_key
    response = pdf_info.process() 
    print(pprint.pformat(json.loads(response.json_content)))


if __name__ == "__main__":
    api_key = 'DP.---API-KEY---'
    basePath = "C:/temp/dynamicpdf-api-samples/"
    run(api_key, basePath)