from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.excel_input import ExcelInput
from dynamicpdf_api.excel_resource import ExcelResource

from Shared import *

def excel_example(apikey, documentPath, outputPath):
    
    pdf=Pdf()
    pdf.api_key=apikey
    pdf.add_excel(ExcelResource(documentPath + "sample-data.xlsx"))       
    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "pdf-excel-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    excel_example(api_key, "./resources/users-guide/", "./output/")