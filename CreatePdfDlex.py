from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from Shared import *

def create_pdf_dlex(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apikey

    layoutDataResource = LayoutDataResource(full_path + "SimpleReportWithCoverPage.json")
    pdf.add_dlex("samples/creating-pdf-pdf-endpoint/SimpleReportWithCoverPage.dlex", layoutDataResource)
    response = pdf.process() 
    if response.is_successful:
         with open(output_path + "create-pdf-dlex-python-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
        print(response.error_message)
        print(response.error_json)
 
if __name__ == "__main__":
    create_pdf_dlex(api_key, base_path + "/creating-pdf-pdf-endpoint/")
