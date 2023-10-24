from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.page_input import PageInput
from dynamicpdf_api.layout_data_resource import LayoutDataResource

def run(apiKey, basePath):
    
    pdf=Pdf()
    pdf.api_key=apiKey

    layout = LayoutDataResource(basePath + "SimpleReportWithCoverPage.json")
    pdf.add_dlex("samples/creating-pdf-pdf-endpoint/SimpleReportWithCoverPage.dlex", layout)

    response = pdf.process() 

    if response.is_successful:
         with open(basePath + "pdf-dlex-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
basePath = "C:/temp/dynamicpdf-api-samples/"
run(api_key, basePath)