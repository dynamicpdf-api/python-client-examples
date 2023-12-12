from dynamicpdf_api.image_resource import ImageResource
from dynamicpdf_api.image_info import ImageInfo
from Shared import *

def image_info(api_key, full_path):
    resource = ImageResource(full_path + "getting-started.png")
    image_info = ImageInfo(resource)
    image_info.api_key = api_key
    response = image_info.process() 
    print(response.json_content)

if __name__ == "__main__":
    image_info(api_key, base_path + "/image-info/")