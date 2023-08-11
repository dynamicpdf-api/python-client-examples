from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource

def merge_pdfs(apiKey):
    
    pdf=Pdf()
    pdf.api_key=apiKey
    inputA = pdf.add_pdf(PdfResource("DocumentA.pdf"))
    inputA.start_page = 1
    inputA.page_count = 1
    pdf.add_pdf(PdfResource("AllFormFields.pdf"))
    pdf.add_pdf("samples/merge-pdfs-pdf-endpoint/DocumentC.pdf")
    response = pdf.process() 
    if response.is_successful:
         with open("Outputs/merge-pdfs-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
merge_pdfs(api_key)