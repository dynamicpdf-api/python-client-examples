from dynamicpdf_api.image_resource import ImageResource
from dynamicpdf_api.image_info import ImageInfo
import pprint
import json

def run(api_key, basePath):
    resource = ImageResource(basePath + "dynamicpdfLogo.png")
    image_info = ImageInfo(resource)
    image_info.api_key = api_key
    response = image_info.process() 
    print(response.json_content)

if __name__ == "__main__":
    api_key = 'DP---API-KEY---'
    basePath = "C:/temp/dynamicpdf-api-samples/"
    run(api_key, basePath)