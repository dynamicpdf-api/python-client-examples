from dynamicpdf_api.dlex_layout import DlexLayout
from dynamicpdf_api.layout_data_resource import LayoutDataResource

def dlex_layout(apiKey, basePath):
    layoutData = LayoutDataResource(basePath + "creating-pdf-dlex-layout.json")
    dlexEndpoint =DlexLayout("samples/creating-pdf-dlex-layout-endpoint/creating-pdf-dlex-layout.dlex", layoutData)
    dlexEndpoint.api_key=apiKey
    response = dlexEndpoint.process() 
    if response.is_successful:
         with open(basePath + "python-dlex-layout-example.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP.xxx-api-key-xxx'
basePath = "C:/temp/dynamicpdf-api-samples/"
dlex_layout(api_key, basePath)