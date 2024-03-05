from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.html_resource import HtmlResource
from Shared import *

def html_example(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apikey

    pdf.add_html("<html><p>This is a test.</p></html>")
    
    with open(full_path + "products.html", 'r', encoding='utf-8') as file:
            htmlString = file.read()
            
    htmlResource = HtmlResource(htmlString)
    pdf.add_html(htmlResource)
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")
    response = pdf.process() 
    
    with open(output_path + "html-output-csharp.pdf", "wb") as output_file:
        output_file.write(response.content)
    
if __name__ == "__main__":
    html_example(api_key, base_path + "/users-guide/")