from dynamicpdf_api.dlex_layout import DlexLayout
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from Shared import *

def dlex_layout(apiKey, full_path):
    layoutData = LayoutDataResource(full_path + "SimpleReportWithCoverPage.json")
    dlexEndpoint =DlexLayout("samples/dlex-layout/SimpleReportWithCoverPage.dlex", layoutData)
    dlexEndpoint.api_key=apiKey
    response = dlexEndpoint.process() 
    if response.is_successful:
         with open(output_path + "python-dlex-layout-example.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    dlex_layout(api_key, base_path + "/dlex-layout/")