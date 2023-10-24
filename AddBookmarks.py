from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.outline_style import OutlineStyle
from dynamicpdf_api.url_action import UrlAction

def bookmark_pdf(apiKey, basePath):
    
    pdf=Pdf()
    pdf.api_key=apiKey

    inputA = pdf.add_pdf(PdfResource(basePath + "DocumentA.pdf"))
    inputA.id="DocumentA"

    inputB = pdf.add_pdf(PdfResource(basePath + "DocumentB.pdf"))
    inputB.id="DocumentB"

    inputC = pdf.add_pdf(PdfResource(basePath + "DocumentC.pdf"))
    inputC.id="DocumentC"

    rootOutline = pdf.outlines.add("Three Bookmarks")
    outlineA = rootOutline.children.add("DocumentA", inputA)
    outlineB = rootOutline.children.add("DocumentB", inputB)
    outlineC = rootOutline.children.add("DocumentC", inputC)
    
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
         with open(basePath + "bookmark-python-output.pdf", "wb") as file:
            file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
basePath = "C:/temp/dynamicpdf-api-samples/"
bookmark_pdf(api_key, basePath)