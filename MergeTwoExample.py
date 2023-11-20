from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource

def merge_pdfs():
    basePath = "C:/temp/dynamicpdf-api-samples/"
    pdf.api_key="DP.xxx-api-key-xxx"
    pdf=Pdf()
    inputA = pdf.add_pdf(PdfResource(basePath + "DocumentA.pdf"))
    pdf.add_pdf(PdfResource(basePath + "DocumentB.pdf"))
    response = pdf.process() 
    if response.is_successful:
         with open(basePath + "merge-pdfs-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)

merge_pdfs()