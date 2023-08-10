from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.page_input import PageInput
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.page_numbering_element import PageNumberingElement

def run(apiKey):
    
    pdf=Pdf()
    pdf.api_key=apiKey
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
         with open("C:/temp/dynamicpdf-api-samples/out/pdf-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
run(api_key)