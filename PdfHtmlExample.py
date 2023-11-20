from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.html_resource import HtmlResource

def merge_pdfs(apiKey):
    
    pdf=Pdf()
    pdf.api_key=apiKey

    pdf.add_html("<html><p>This is a test.</p></html>")
    pdf.add_html(HtmlResource("html.html", "rb"))
    pdf.add_html("<html><img src='./images/logo.png'></img></html>", "https://www.dynamicpdf.com")
    response = pdf.process() 
    
    with open("Outputs/html-output-csharp.pdf", "wb") as output_file:
        output_file.write(response.content)
    
# Call the function
api_key = 'DP.xxx-api-key-xxx'
merge_pdfs(api_key)