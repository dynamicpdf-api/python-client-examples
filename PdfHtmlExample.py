from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.html_resource import HtmlResource
from Shared import *

def html_example(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apikey

    pdf.add_html("<html><p>This is a test.</p></html>")
    pdf.add_html(HtmlResource("html.html", "rb"))
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")
    response = pdf.process() 
    
    with open(output_path + "html-output-csharp.pdf", "wb") as output_file:
        output_file.write(response.content)
    
if __name__ == "__main__":
    html_example(api_key, base_path + "/pdf-html-example/")