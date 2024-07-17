from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.image_resource import ImageResource
from dynamicpdf_api.word_resource import WordResource
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from dynamicpdf_api.html_resource import HtmlResource
from Shared import *

def merge_solution(apikey, base_path, output_path):
    pdf=Pdf()
    pdf.api_key=apikey
    inputA = pdf.add_pdf(PdfResource(base_path + "merge-pdfs-pdf-endpoint/DocumentA.pdf"))
    inputA.start_page = 1
    inputA.page_count = 2
    pdf.add_pdf(PdfResource(base_path + "merge-pdfs-pdf-endpoint/DocumentB.pdf"))
   
    pdf.add_word(WordResource(base_path + "users-guide/Doc1.docx"))

    imageResource = ImageResource(base_path + "image-conversion/testimage.tif")
    imageInput =  pdf.add_image(imageResource)
    
    layoutData = LayoutDataResource(base_path + "creating-pdf-dlex-layout/creating-pdf-dlex-layout.json")
    
    pdf.add_dlex("samples/creating-pdf-dlex-layout-endpoint/creating-pdf-dlex-layout.dlex", layoutData)
    
    with open(base_path + "users-guide/products.html", 'r', encoding='utf-8') as file:
            htmlString = file.read()
            
    htmlResource = HtmlResource(htmlString)
    pdf.add_html(htmlResource)
    
    response = pdf.process() 
    
    if response.is_successful:
         with open(output_path + "merge-solution-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)

if __name__ == "__main__":
    merge_solution(api_key, base_path, output_path)