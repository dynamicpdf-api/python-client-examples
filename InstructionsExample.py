from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_response import PdfResponse
from dynamicpdf_api.page_input import PageInput
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.aes256_security import Aes256Security
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.text_element import TextElement
from dynamicpdf_api.elements.page_numbering_element import PageNumberingElement
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.html_resource import HtmlResource
from dynamicpdf_api.form_field import FormField
from dynamicpdf_api.template import Template
from dynamicpdf_api.elements.aztec_barcode_element import AztecBarcodeElement
from dynamicpdf_api.dlex_resource import DlexResource
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from dynamicpdf_api.image_resource import ImageResource
import json
import re
import io

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

def AcroFormExample(apiKey):
    pdf=Pdf()
    pdf.api_key = apiKey
    pdf.add_pdf("samples/users-guide-resources/simple-form-fill.pdf");
    formField = FormField("nameField", "DynamicPDF");
    formField2 = FormField("descriptionField", "DynamicPDF CloudAPI. RealTime PDFs, Real FAST!");
    pdf.form_fields.append(formField)
    pdf.form_fields.append(formField2)
    return pdf



def AddOutlinesForNewPdf(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
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
    return pdf

def AddOutlinesExistingPdf(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    pdf.author = "John Doe"
    pdf.title = "Sample Pdf"
    resource = PdfResource("C:/temp/users-guide-resources/AllPageElements.pdf")
    input = pdf.add_pdf(resource)
    input.id = "AllPageElements"
    resource1 = PdfResource("C:/temp/users-guide-resources/OutlineExisting.pdf")
    input1 = pdf.add_pdf(resource1)
    input1.id = "outlineDoc1"

    rootOutline = pdf.outlines.add("Imported Outline")
    rootOutline.expanded = True
    rootOutline.children.add(input)
    rootOutline.children.add(input1)
    return pdf

def TemplateExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    resource = PdfResource("C:/temp/merge-pdf/DocumentA.pdf")
    input = pdf.add_pdf(resource)

    template = Template("Temp1")
    element = TextElement("Hello World", ElementPlacement.TopCenter)
    template.elements.append(element)
    input.template = template
    return pdf

def BarcodeExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    resource = PdfResource("C:/temp/merge-pdf/DocumentA.pdf")
    input = pdf.add_pdf(resource)
    template = Template("Temp1")
    element = AztecBarcodeElement("Hello World", ElementPlacement.TopCenter, 0, 500)
    template.elements.append(element)
    input.template = template
    return pdf

def DlexPdfExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    layout = LayoutDataResource("c:/temp/dlex-resource/SimpleReportWithCoverPage.json")
    pdf.add_dlex("samples/dlex-layout/SimpleReportWithCoverPage.dlex", layout)
    return pdf

def DlexPdfStringExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
   
    with open("c:/temp/dlex-resource/SimpleReportWithCoverPage.json","r") as f:
        fileData = f.read()

    f.close()
    python_obj = json.loads(fileData)
    layout = LayoutDataResource(python_obj)
    pdf.add_dlex("samples/dlex-layout/SimpleReportWithCoverPage.dlex", layout)
    return pdf

def ImageExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey

    #read image as binary stream

    with io.open("c:/temp/users-guide-resources/A.png", 'rb') as f:
        imageBinary = f.read()

    imageStream = io.BytesIO(imageBinary)
    f.close()
    imageResource = ImageResource(imageStream)
    pdf.add_image(imageResource)


    #get image from cloud storage

    pdf.add_image("samples/users-guide-resources/B.png")

    #get image from local file

    imageFile = "c:/temp/users-guide-resources/C.png"
    imageResource2 = ImageResource(imageFile)
    pdf.add_image(imageResource2)

    return pdf

def HtmlExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    pdf.add_html("<html><p>Welcome to DynamicPDF Cloud API.</p></html>")

    with open("c:/temp/users-guide-resources/products.html","rt") as f:
        fileData = f.read()
    f.close()

    pdf.add_html(fileData)
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")

    return pdf




def PageExample(apiKey):
    pdf = Pdf()
    pdf.api_key = apiKey
    pageInput = pdf.add_page(1008, 612)

    textElement = TextElement("Hello from DynamicPDF Cloud API.", ElementPlacement.TopCenter)
    pageNumberingElement = PageNumberingElement("A", ElementPlacement.TopRight)
    pageNumberingElement.color = RgbColor.red()    
    pageNumberingElement.font = Font.courier()
    pageNumberingElement.font_size = 42

    pageInput.elements.append(pageNumberingElement)
    pageInput.elements.append(textElement)

    return pdf

def PdfExample(apiKey):
    pdf=Pdf()
    pdf.api_key=apiKey
    inputA = pdf.add_pdf(PdfResource("c:/temp/users-guide-resources/DocumentA.pdf"))

  #read pdf as binary stream

    with io.open("c:/temp/users-guide-resources/DocumentB.pdf", 'rb') as f:
        pdfBinary = f.read()

    pdfStream = io.BytesIO(pdfBinary)
    f.close()

    pdf.add_pdf(PdfResource(pdfStream))
    pdf.add_pdf("samples/users-guide-resources/DocumentC.pdf")
    
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
    #pdf = MergePdfs(apiKey)
    #pdf = AcroFormExample(apiKey)
    #pdf = AddOutlinesForNewPdf(apiKey)
    #pdf = AddOutlinesExistingPdf(apiKey)
    #pdf = TemplateExample(apiKey)
    #pdf = BarcodeExample(apiKey)
    #pdf = DlexPdfExample(apiKey)
    #pdf = DlexPdfStringExample(apiKey)
    #pdf = ImageExample(apiKey)
    #pdf = HtmlExample(apiKey)
    #pdf = PageExample(apiKey)
    pdf = PdfExample(apiKey)

    response = pdf.process()
    if response.is_successful:
        outputResult(basePathOut, "pdf-python-out.pdf", response)
    else:
        print(response.error_json) 
    

if __name__ == "__main__":
    api_key = "DP.---API-KEY---"
    run(api_key)