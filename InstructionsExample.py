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
from dynamicpdf_api.word_input import WordInput
from dynamicpdf_api.word_resource import WordResource
import json
import re
import io

def TopLevelMetaData():
    pdf = Pdf()
    pdf.add_page(1008, 612)
    pdf.author = "John Doe"
    pdf.keywords ="dynamicpdf api example pdf java instructions"
    pdf.creator = "John Creator"
    pdf.subject = "topLevel document metadata"
    pdf.title = "Sample PDF"
    return pdf

def FontsExample(basePath):
    pdf = Pdf()
    pageInput = pdf.add_page(1008, 612)
    pageNumberingElement = PageNumberingElement("A", ElementPlacement.TopRight)
    pageNumberingElement.color = RgbColor.red()    
    pageNumberingElement.font = Font.courier()
    pageNumberingElement.font_size = 42
   

    cloudResourceName = "samples/users-guide-resources/Calibri.otf"
    pageNumberingElementTwo = PageNumberingElement("B", ElementPlacement.TopLeft)
    pageNumberingElementTwo.color = RgbColor.dark_orange()
    pageNumberingElementTwo.font = Font(cloudResourceName)
    pageNumberingElementTwo.fontSize = 32

    pageNumberingElementThree = PageNumberingElement("C", ElementPlacement.TopCenter)
    pageNumberingElementThree.color = RgbColor.green()
    pageNumberingElementThree.font = Font.from_file(basePath + "cnr.otf")
    pageNumberingElementThree.fontSize = 42

    pageInput.elements.append(pageNumberingElement)
    pageInput.elements.append(pageNumberingElementTwo)
    pageInput.elements.append(pageNumberingElementThree)

    return pdf

def WordExample(documentPath):
    pdf=Pdf()
    fileResource = documentPath
    wordResource = WordResource(documentPath + "Doc1.docx")       
    word = WordInput(wordResource)
    word.page_width = 300
    word.page_height = 200

    word.top_margin = 10
    word.bottom_margin = 10
    word.right_margin = 40
    word.left_margin = 40
    pdf.inputs.append(word)
    return pdf

def SecurityExample(documentPath):
    fileResource = documentPath + "DocumentB.pdf"
    userName = "myuser"
    passWord = "mypassword"
    pdf = Pdf()
    resource = PdfResource(fileResource)
    pdf.add_pdf(resource)
    sec = Aes256Security(userName, passWord)
    sec.allow_copy = False
    sec.allow_print = False
    pdf.security = sec
    return pdf

def HtmlExample(documentPath):
    pdf = Pdf()
    pdf.add_html("<html><p>Welcome to DynamicPDF Cloud API.</p></html>")
    
    with open(documentPath + "products.html","rt") as f:
        fileData = f.read()
        f.close()

    pdf.add_html(fileData)
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")
    return pdf

def MergePdfs(documentPath):
    pdf=Pdf()
    resourceOne = PdfResource(documentPath + "DocumentA.pdf")
    pdf.add_pdf(resourceOne)
    pdf.add_image("samples/get-image-info-image-info-endpoint/dynamicpdfLogo.png")
    resourceTwo = PdfResource(documentPath + "DocumentB.pdf")
    pdf.add_pdf(resourceTwo)
    return pdf

def AcroFormExample():
    pdf=Pdf()
    pdf.add_pdf("samples/users-guide-resources/simple-form-fill.pdf");
    formField = FormField("nameField", "DynamicPDF");
    formField2 = FormField("descriptionField", "DynamicPDF CloudAPI. RealTime PDFs, Real FAST!");
    pdf.form_fields.append(formField)
    pdf.form_fields.append(formField2)
    return pdf

def AddOutlinesForNewPdf():
    pdf = Pdf()
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

def AddOutlinesExistingPdf(documentPath):
    pdf = Pdf()
    pdf.author = "John Doe"
    pdf.title = "Sample Pdf"
    resource = PdfResource(documentPath + "AllPageElements.pdf")
    input = pdf.add_pdf(resource)
    input.id = "AllPageElements"
    resource1 = PdfResource(documentPath + "OutlineExisting.pdf")
    input1 = pdf.add_pdf(resource1)
    input1.id = "outlineDoc1"

    rootOutline = pdf.outlines.add("Imported Outline")
    rootOutline.expanded = True
    rootOutline.children.add(input)
    rootOutline.children.add(input1)
    return pdf

def TemplateExample(documentPath):
    pdf = Pdf()
    resource = PdfResource(documentPath + "DocumentA.pdf")
    input = pdf.add_pdf(resource)

    template = Template("Temp1")
    element = TextElement("Hello World", ElementPlacement.TopCenter)
    template.elements.append(element)
    input.template = template
    return pdf

def BarcodeExample(documentPath):
    pdf = Pdf()
    resource = PdfResource(documentPath + "DocumentA.pdf")
    input = pdf.add_pdf(resource)
    template = Template("Temp1")
    element = AztecBarcodeElement("Hello World", ElementPlacement.TopCenter, 0, 500)
    template.elements.append(element)
    input.template = template
    return pdf

def DlexPdfExample(documentPath):
    pdf = Pdf()
    layout = LayoutDataResource(documentPath + "SimpleReportWithCoverPage.json")
    pdf.add_dlex("samples/users-guide-resources/SimpleReportWithCoverPage.dlex", layout)
    return pdf

def DlexPdfStringExample(documentPath):
    pdf = Pdf()
   
    with open(documentPath + "SimpleReportWithCoverPage.json","r") as f:
        fileData = f.read()

    f.close()
    python_obj = json.loads(fileData)
    layout = LayoutDataResource(python_obj)
    pdf.add_dlex("samples/users-guide-resources/SimpleReportWithCoverPage.dlex", layout)
    return pdf

def ImageExample(documentPath):
    pdf = Pdf()

    #read image as binary stream

    with io.open(documentPath + "A.png", 'rb') as f:
        imageBinary = f.read()

    imageStream = io.BytesIO(imageBinary)
    f.close()
    imageResource = ImageResource(imageStream)
    pdf.add_image(imageResource)


    #get image from cloud storage

    pdf.add_image("samples/users-guide-resources/B.png")

    #get image from local file

    imageFile = documentPath + "C.png"
    imageResource2 = ImageResource(imageFile)
    pdf.add_image(imageResource2)

    return pdf

def HtmlExample(documentPath):
    pdf = Pdf()
    pdf.add_html("<html><p>Welcome to DynamicPDF Cloud API.</p></html>")

    with open(documentPath + "products.html","rt") as f:
        fileData = f.read()
    f.close()

    pdf.add_html(fileData)
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")

    return pdf

def PageExample():
    pdf = Pdf()
    pageInput = pdf.add_page(1008, 612)

    textElement = TextElement("Hello from DynamicPDF Cloud API.", ElementPlacement.TopCenter)
    pageNumberingElement = PageNumberingElement("A", ElementPlacement.TopRight)
    pageNumberingElement.color = RgbColor.red()    
    pageNumberingElement.font = Font.courier()
    pageNumberingElement.font_size = 42

    pageInput.elements.append(pageNumberingElement)
    pageInput.elements.append(textElement)

    return pdf

def PdfExample(documentPath):
    pdf=Pdf()
    inputA = pdf.add_pdf(PdfResource(documentPath + "DocumentA.pdf"))

  #read pdf as binary stream

    with io.open(documentPath + "DocumentB.pdf", 'rb') as f:
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

def outputPdf(pdf:Pdf, apiKey, baseOutputPath, outputFile):
    pdf.api_key = apiKey
    response = pdf.process()
    if response.is_successful:
        outputResult(baseOutputPath, outputFile, response)
    else:
        print(response.error_message)
        print(response.error_json) 

def run(apiKey):    
    basePathOut = "c:/temp/dynamicpdf-api-usersguide-examples/python-output/"
    basePathIn = "c:/temp/users-guide-resources/"
    pdf = TopLevelMetaData()
    outputPdf(pdf, apiKey, basePathOut, "top-level-metadata-out.pdf")
    pdf = FontsExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "fonts-out.pdf")
    pdf = SecurityExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "security-out.pdf")
    pdf = HtmlExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "html-out.pdf")
    pdf = MergePdfs(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "merge-out.pdf")
    pdf = AcroFormExample()
    outputPdf(pdf, apiKey, basePathOut, "acroform-out.pdf")
    pdf = AddOutlinesForNewPdf()
    outputPdf(pdf, apiKey, basePathOut, "outlines-out.pdf")
    pdf = AddOutlinesExistingPdf(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "outlines-existing-out.pdf")
    pdf = TemplateExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "template-out.pdf")
    pdf = BarcodeExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "barcode-out.pdf")
    pdf = DlexPdfExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "dlex-out.pdf")
    pdf = DlexPdfStringExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "dlex-string-out.pdf")
    pdf = ImageExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "top-level-metadata-out.pdf")
    pdf = HtmlExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "image-out.pdf")
    pdf = PageExample()
    outputPdf(pdf, apiKey, basePathOut, "page-out.pdf")
    pdf = PdfExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "pdf-out.pdf")
    pdf = WordExample(basePathIn)
    outputPdf(pdf, apiKey, basePathOut, "word-out.pdf")
    

if __name__ == "__main__":
    api_key = "DP.xxx-api-key-xxx"
    run(api_key)