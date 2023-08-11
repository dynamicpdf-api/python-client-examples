from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.layout_data_resource import LayoutDataResource

def merge_pdfs(apiKey):
    
    pdf=Pdf()
    pdf.api_key=apiKey

    layoutDataResource = LayoutDataResource("SimpleReportWithCoverPage.json")
    pdf.add_dlex("samples/creating-pdf-pdf-endpoint/SimpleReportWithCoverPage.dlex", layoutDataResource)
    response = pdf.process() 
    if response.is_successful:
         with open("Outputs/create-pdf-dlex-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
merge_pdfs(api_key)
