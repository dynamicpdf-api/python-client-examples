from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from Shared import *

def split_pdf(apikey, full_path):
    pdf=Pdf()
    pdf.api_key=apikey

    split(pdf, full_path, 1, 3, "splitpdf-one.pdf")
    split(pdf, full_path, 6, 2, "splitpdf-two.pdf")

    response = pdf.process() 

def split(pdf, full_path, startPage, pageCount, outputFile):

    inputA = pdf.add_pdf(PdfResource(full_path + "pdfnumberedinput.pdf"))
    inputA.start_page = startPage
    inputA.page_count = pageCount
    
    response = pdf.process() 

    if response.is_successful:
         with open(output_path + outputFile, "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)

if __name__ == "__main__":
    split_pdf(api_key, base_path + "/split-pdf/")