from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.page_input import PageInput
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from Shared import *

def pdf_dlex_example(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apikey

    layout = LayoutDataResource(full_path + "SimpleReportWithCoverPage.json")
    pdf.add_dlex("samples/creating-pdf-pdf-endpoint/SimpleReportWithCoverPage.dlex", layout)

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "pdf-dlex-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    pdf_dlex_example(api_key, base_path + "/creating-pdf-pdf-endpoint/")