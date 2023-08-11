from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.outline_style import OutlineStyle
from dynamicpdf_api.url_action import UrlAction

def bookmark_pdf(apiKey):
    
    pdf=Pdf()
    pdf.api_key=apiKey

    inputA = pdf.add_pdf(PdfResource("AllFormFields.pdf"))
    inputA.id="AllFormFields"

    inputB = pdf.add_pdf(PdfResource("AllPageElements.pdf"))
    inputB.id="AllPageElements"

    inputC = pdf.add_pdf(PdfResource("DocumentA.pdf"))
    inputC.id="DocumentA"

    rootOutline = pdf.outlines.add("Three Bookmarks")
    outlineA = rootOutline.children.add("AllFormFields", inputA)
    outlineB = rootOutline.children.add("AllPageElements", inputB)
    outlineC = rootOutline.children.add("DocumentA", inputC)
    
    rootOutline.color = RgbColor.red()
    rootOutline.style = OutlineStyle.BoldItalic
    outlineA.color = RgbColor.orange()
    outlineB.color = RgbColor.green()
    outlineC.color = RgbColor.purple()

    outlineD = rootOutline.children.add("DynamicPDF Cloud API")
    outlineD.color = RgbColor.blue()
    outlineD.action = UrlAction("https://cloud.dynamicpdf.com/")

    rootOutline.expanded = True
    
    response = pdf.process() 
    if response.is_successful:
         with open("Outputs/bookmark-python.pdf", "wb") as file:
            file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
bookmark_pdf(api_key)