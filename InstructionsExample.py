from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_response import PdfResponse
from dynamicpdf_api.page_input import PageInput
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.aes256_security import Aes256Security
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.page_numbering_element import PageNumberingElement
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.html_resource import HtmlResource


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

def SecurityExample(apiKey, documentPath):
    fileResource = documentPath
    userName = "myuser"
    passWord = "mypassword"
    pdf = Pdf()
    pdf.api_key = apiKey
    resource = PdfResource(documentPath)
    pdf.add_pdf(resource)
    sec = Aes256Security(userName, passWord)
    sec.allow_copy = False
    sec.allow_print = False
    pdf.security = sec
    return pdf

def HtmlExample(apiKey):
    pdf=Pdf()
    pdf.api_key=apiKey
    pdf.add_html("<html><p>This is a test.</p></html>")
    pdf.add_html(HtmlResource("html.html", "rb"))
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")
    return pdf

def MergePdfs(apiKey):
    pdf=Pdf()
    pdf.api_key=apiKey
    resourceOne = PdfResource("C:/temp/merge-pdf/DocumentA.pdf")
    pdf.add_pdf(resourceOne)
    pdf.add_image("samples/get-image-info-image-info-endpoint/dynamicpdfLogo.png")
    resourceTwo = PdfResource("C:/temp/merge-pdf/DocumentB.pdf")
    pdf.add_pdf(resourceTwo)
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
    #pdf = FontsExample(apiKey, "C:/temp/fonts-example/cnr.otf")
    #pdf = SecurityExample(apiKey, "C:/temp/merge-pdf/DocumentA.pdf")
    #pdf = HtmlExample(apiKey)
    pdf = MergePdfs(apiKey)
    response = pdf.process() 
    outputResult(basePathOut, "pdf-python-out.pdf", response)

if __name__ == "__main__":
    api_key = "DP---API-KEY---"
    run(api_key)