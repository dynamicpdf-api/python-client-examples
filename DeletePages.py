from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from Shared import *

def delete_pages(apikey, full_path):
    pdf=Pdf()
    pdf.api_key=apikey
    inputA = pdf.add_pdf(PdfResource(full_path + "pdfnumberedinput.pdf"))
    inputA.start_page = 1
    inputA.page_count = 3
    
    inputB = pdf.add_pdf(PdfResource(full_path + "pdfnumberedinput.pdf"))
    inputB.start_page = 6
    inputB.page_count = 2

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "delete-pages-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)

if __name__ == "__main__":
    delete_pages(api_key, base_path + "/delete-pages/")