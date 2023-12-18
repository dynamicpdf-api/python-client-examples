from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from Shared import *

def merge_pdfs(apikey, full_path):
    pdf=Pdf()
    pdf.api_key=apikey
    inputA = pdf.add_pdf(PdfResource(full_path + "DocumentA.pdf"))
    inputA.start_page = 1
    inputA.page_count = 2
    pdf.add_pdf(PdfResource(full_path + "DocumentB.pdf"))
    pdf.add_pdf("samples/merge-pdfs-pdf-endpoint/DocumentC.pdf")
    response = pdf.process() 
    if response.is_successful:
         with open(output_path + "merge-pdfs-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)

if __name__ == "__main__":
    merge_pdfs(api_key, base_path + "/merge-pdfs-pdf-endpoint/")