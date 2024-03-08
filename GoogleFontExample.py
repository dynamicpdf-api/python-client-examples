from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.text_element import TextElement
from Shared import *

def google_example(apikey):
    
    pdf=Pdf()
    pdf.api_key=apikey
  
    inputPage = pdf.add_page()
    element = TextElement("Hello", ElementPlacement.TopCenter, 150, 250)
    element.color = RgbColor.blue_violet()
    element.font = Font.google("Anta", False, False)
    element.font_size = 45
    inputPage.elements.append(element)
    
    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "google-font-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    google_example(api_key)