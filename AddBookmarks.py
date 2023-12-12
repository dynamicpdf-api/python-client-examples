from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.outline_style import OutlineStyle
from dynamicpdf_api.url_action import UrlAction
from Shared import *

def bookmark_pdf(apiKey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apiKey

    inputA = pdf.add_pdf(PdfResource(full_path + "DocumentA.pdf"))
    inputA.id="DocumentA"

    inputB = pdf.add_pdf(PdfResource(full_path + "DocumentB.pdf"))
    inputB.id="DocumentB"

    inputC = pdf.add_pdf(PdfResource(full_path + "DocumentC.pdf"))
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
         with open(full_path + "bookmark-python-output.pdf", "wb") as file:
            file.write(response.content)
    else:
        print(response.error_id)

if __name__ == "__main__":
    bookmark_pdf(api_key, base_path + "/add-bookmarks/")