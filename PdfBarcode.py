from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.code11_barcode_element import Code11BarcodeElement
from Shared import *

def pdfbarcode_example(apikey):
    
    pdf=Pdf()
    pdf.api_key = apikey
    pdf.author = "John Doe"
    pdf.title = "My PDF"
    inputPage = pdf.add_page(1008, 612)
    
    code11BarcodeElement = Code11BarcodeElement("12345678", ElementPlacement.TopCenter, 200, 50, 50)
    code11BarcodeElement.color = RgbColor.red()
	
    inputPage.elements.append(code11BarcodeElement)

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "barcode-pdf-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    pdfbarcode_example(api_key)