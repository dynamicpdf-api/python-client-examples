from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.html_resource import HtmlResource
from dynamicpdf_api.page_size import PageSize
from dynamicpdf_api.page_orientation import PageOrientation

def PDfHtmlCssWorkAround(api_key):
    pdf = Pdf()
    pdf.api_key = api_key
    
    with open("c:/temp/users-guide-resources/example.html","r") as f:
        tempHtml = f.read()
        f.close()
    with open("c:/temp/users-guide-resources/example.css","r") as g:
        tempCss = g.read()
        g.close()
    
    sb1 = tempHtml[0:tempHtml.index("<link"):1];
    sb2 = tempHtml[tempHtml.index("/>") + 2::];
    sb = sb1 + "<style>" + tempCss + "</style>" + sb2;
    print(sb);
    resource = HtmlResource(sb);
    pdf.add_html(resource, None, PageSize.Letter, PageOrientation.Portrait,1);

    response = pdf.process()

    if response.is_successful:
        with open("c:/temp/dynamicpdf-api-usersguide-examples/python-output/workaround-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_json)

PDfHtmlCssWorkAround("DP.f9wgIYZzDrTajG2MSAWUdh1m7YJ1+iexxbkV/15t0l3TR5oaxRjdGCC1")