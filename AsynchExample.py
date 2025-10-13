import asyncio
from dynamicpdf_api.dlex_layout import DlexLayout
from dynamicpdf_api.layout_data_resource import LayoutDataResource
from Shared import *  # I assume this defines api_key, base_path, output_path, etc.

async def async_dlex_layout(apiKey, full_path):
    layoutData = LayoutDataResource(full_path + "creating-pdf-dlex-layout.json")
    dlexEndpoint = DlexLayout("samples/creating-pdf-dlex-layout-endpoint/creating-pdf-dlex-layout.dlex", layoutData)
    dlexEndpoint.api_key = apiKey

    # Await the asynchronous call
    response = await dlexEndpoint.process_async()

    if response.is_successful:
        with open(output_path + "python-async-example.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print("Error:", response.error_id, response.error_message if hasattr(response, "error_message") else "")

def main():
    # Use asyncio to run the async function
    asyncio.run(async_dlex_layout(api_key, base_path + "creating-pdf-dlex-layout/"))

if __name__ == "__main__":
    main()
