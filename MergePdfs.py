from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource

def merge_pdfs():
    basePath = "C:/temp/dynamicpdf-api-samples/"
    pdf=Pdf()
    pdf.api_key="DP.25DHurNAMB8MEgzPg3mmUyBsjkqQbjgVAZuFuu4ynh6OSaBCOp6JIrR7"
    inputA = pdf.add_pdf(PdfResource(basePath + "DocumentA.pdf"))
    inputA.start_page = 1
    inputA.page_count = 2
    pdf.add_pdf(PdfResource(basePath + "DocumentB.pdf"))
    pdf.add_pdf("samples/merge-pdfs-pdf-endpoint/DocumentC.pdf")
    response = pdf.process() 
    if response.is_successful:
         with open(basePath + "merge-pdfs-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)

merge_pdfs()