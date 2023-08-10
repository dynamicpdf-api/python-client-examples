from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_response import PdfResponse
from dynamicpdf_api.page_input import PageInput
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.page_numbering_element import PageNumberingElement

def TopLevelMetaData(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    pdf.add_page(1008, 612)
    pdf.author = "John Doe"
    pdf.keywords ="dynamicpdf api example pdf java instructions"
    pdf.creator = "John Creator"
    pdf.subject = "topLevel document metadata"
    pdf.title = "Sample PDF"
    return pdf

def FontsExample(apiKey, fontPath):
    pdf = Pdf()
    pdf.api_key = apiKey
    pageInput = pdf.add_page(1008, 612)

    pageNumberingElement = PageNumberingElement("A", ElementPlacement.TopRight)
    pageNumberingElement.color = RgbColor.red()    
    pageNumberingElement.font = Font.courier()
    pageNumberingElement.font_size = 42
   

    cloudResourceName = "samples/fonts-example/Calibri.otf"
    pageNumberingElementTwo = PageNumberingElement("B", ElementPlacement.TopLeft)
    pageNumberingElementTwo.color = RgbColor.dark_orange()
    pageNumberingElementTwo.font = Font(cloudResourceName)
    pageNumberingElementTwo.fontSize = 32

    pageNumberingElementThree = PageNumberingElement("C", ElementPlacement.TopCenter)
    pageNumberingElementThree.color = RgbColor.green()
    pageNumberingElementThree.font = Font.from_file(fontPath)
    pageNumberingElementThree.fontSize = 42

    pageInput.elements.append(pageNumberingElement)
    pageInput.elements.append(pageNumberingElementTwo)
    pageInput.elements.append(pageNumberingElementThree)

    return pdf


def outputResult(outputPath, fileName, response:PdfResponse) :
    if response.is_successful:
         with open(outputPath + fileName, "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_json)



def run(apiKey):    
    basePathOut = "C:/temp/instructions-example/out/"
    #pdf = TopLevelMetaData(apiKey)
    pdf = FontsExample(apiKey, "C:/temp/fonts-example/cnr.otf")

    response = pdf.process() 
    outputResult(basePathOut, "pdf-python-out.pdf", response)

if __name__ == "__main__":
    api_key = "DP---API-KEY---"
    run(api_key)