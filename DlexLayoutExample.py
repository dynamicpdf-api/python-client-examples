from dynamicpdf_api.dlex_layout import DlexLayout
from dynamicpdf_api.dlex_resource import DlexResource
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from Shared import *

def dlex_layout(apiKey, full_path):
    dlex_layout_cloud(apiKey, full_path)
    dlex_layout_local(apiKey, full_path)

def dlex_layout_cloud(apiKey, full_path):
    layoutData = LayoutDataResource(full_path + "SimpleReportWithCoverPage.json")
    dlexEndpoint =DlexLayout("samples/dlex-layout/SimpleReportWithCoverPage.dlex", layoutData)
    dlexEndpoint.api_key=apiKey
    response = dlexEndpoint.process() 
    if response.is_successful:
         with open(output_path + "python-dlex-layout-example.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)

def dlex_layout_local(apiKey, full_path):
    layoutData = LayoutDataResource(full_path + "SimpleReportWithCoverPage.json")
    dlexResource = DlexResource(full_path + "SimpleReportWithCoverPage.dlex", "SimpleReportWithCoverPage.dlex")
    dlexEndpoint =DlexLayout(dlexResource, layoutData)
    dlexEndpoint.add_additional_resource(full_path + "NorthwindLogo.gif")
    dlexEndpoint.api_key=apiKey
    response = dlexEndpoint.process() 
    if response.is_successful:
         with open(output_path + "python-dlex-layout-local-example.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    dlex_layout(api_key, base_path + "/dlex-layout/")