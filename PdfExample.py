from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.page_numbering_element import PageNumberingElement
from Shared import *

def pdf_example(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apikey
    pdf.author = "John Doe"
    pdf.title = "My Blank PDF Page"
    inputPage = pdf.add_page(1008, 612)
    
    pageNumberingElement = PageNumberingElement("1", ElementPlacement.TopRight)
    pageNumberingElement.color = RgbColor.red()    
    pageNumberingElement.font = Font.courier()
    pageNumberingElement.font_size = 72
    inputPage.elements.append(pageNumberingElement)

    response = pdf.process() 

    if response.is_successful:
         with open(full_path + "pdf-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    pdf_example(api_key, base_path + "/pdf-example/")