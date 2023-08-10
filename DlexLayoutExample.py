from dynamicpdf_api.dlex_layout import DlexLayout
from dynamicpdf_api.layout_data_resource import LayoutDataResource

def dlex_layout(apiKey):
    layoutData = LayoutDataResource("C:/temp/dlex-layout-example/SimpleReportWithCoverPage.json")
    dlexEndpoint =DlexLayout("samples/dlex-layout/SimpleReportWithCoverPage.dlex", layoutData)
    dlexEndpoint.api_key=apiKey
    response = dlexEndpoint.process() 
    if response.is_successful:
         with open("C:/temp/dlex-layout-example/python-dlex-layout-example.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP---API-KEY---'
dlex_layout(api_key)