from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.image_resource import ImageResource
from dynamicpdf_api.image_input import ImageInput
from dynamicpdf_api.v_align import VAlign
from dynamicpdf_api.align import Align


from Shared import *

def image_conversion_example(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key = apikey
    pdf.author = "John Doe"
    pdf.title = "My Blank PDF Page"

    imageResource = ImageResource(full_path + "testimage.tif")
    imageResource2 = ImageResource(full_path + "dynamicpdfLogo.png")

    imageInput =  pdf.add_image(imageResource)
    imageInput.expand_to_fit = False
    imageInput.page_width = 612
    imageInput.page_height = 1008
    imageInput.v_align = VAlign.Center
    imageInput.align = Align.Center
    
    imageInput2 = pdf.add_image(imageResource2)
    imageInput2 = ImageInput(imageResource)
    imageInput2.expand_to_fit = True
    imageInput2.page_width = 1008
    imageInput2.page_height = 612
    imageInput2.v_align = VAlign.Center
    imageInput2.align = Align.Center

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "image-conversion.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    image_conversion_example(api_key, base_path + "/image-conversion/")