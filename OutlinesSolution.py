from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.text_element import TextElement
from dynamicpdf_api.pdf_resource import PdfResource
from Shared import *

def outlines_solution(apikey, full_path):
    pdf = Pdf()
    pdf.api_key = apikey
    pdf.author = "John Doe"
    pdf.title = "Sample Pdf"
    pageInput = pdf.add_page()
    element = TextElement("Hello World 1", ElementPlacement.TopCenter)
    pageInput.elements.append(element)
    pageInput1 = pdf.add_page()
    element1 = TextElement("Hello World 2", ElementPlacement.TopCenter)
    pageInput2 = pdf.add_page()
    element2 = TextElement("Hello World 3", ElementPlacement.TopCenter)
    pageInput2.elements.append(element2)
    rootOutline = pdf.outlines.add("Root Outline")
    rootOutline.children.add("Page 1", pageInput)
    rootOutline.children.add("Page 2", pageInput1)
    rootOutline.children.add("Page 3", pageInput2)

    inputA = pdf.add_pdf(PdfResource(full_path + "PdfOutlineInput.pdf"))
    inputA.id = "pdfoutlineinput"
    rootOutline.children.add_pdf_outlines(inputA)
    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "outlines-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    outlines_solution(api_key, base_path + "/outlines/")