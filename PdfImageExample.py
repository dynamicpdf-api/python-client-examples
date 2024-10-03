from dynamicpdf_api.imaging.pdf_image import PdfImage
from dynamicpdf_api.imaging.png_image_format import PngImageFormat
from dynamicpdf_api.pdf_resource import PdfResource
import pprint
import json
import base64
from Shared import *

def pdf_image_example(api_key, full_path):
    pdf_image_process(api_key, full_path + "onepage.pdf", "pdf-image-out-")
    pdf_image_process(api_key, full_path + "pdfnumberedinput.pdf", "pdf-multi-image-out-")


def pdf_image_process(api_key, full_path, outfile_name):
    resource = PdfResource(full_path)
    pdf_image = PdfImage(resource)
    pdf_image.api_key = api_key
    pdf_image.image_format = PngImageFormat()
    response = pdf_image.process()
    
    if response.is_successful:
         for i, image in enumerate(response.images):
            file_name = output_path + outfile_name + str(i) + ".png"
            with open(file_name , "wb") as out_stream:
                out_stream.write(base64.b64decode(image.data))
    else:
        print(pprint.pformat(json.loads(response.json_content)))


if __name__ == "__main__":
    pdf_image_example(api_key, base_path + "/pdf-image/", )