from dynamicpdf_api.pdf_info import PdfInfo
from dynamicpdf_api.pdf_resource import PdfResource
import pprint
import json

def run(api_key):
    resource = PdfResource("C:/temp/dynamicpdf-api-samples/pdf-info/fw4.pdf")
    pdf_info = PdfInfo(resource)
    pdf_info.api_key = api_key
    response = pdf_info.process() 
    print(pprint.pformat(json.loads(response.json_content)))


if __name__ == "__main__":
    api_key = "DP.jp1OeWjCQG0FCbkUt7MGXeJCXXEAjy7C5iSJNBNnKzJ9Q5Ss8+SjczcH"
    run(api_key)