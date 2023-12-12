from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.html_resource import HtmlResource
from dynamicpdf_api.page_size import PageSize
from dynamicpdf_api.page_orientation import PageOrientation
from Shared import *

def html_css_work_around(api_key, full_path, output_path):

    pdf = Pdf()
    pdf.api_key = api_key
    
    with open(full_path + "example.html","r") as f:
        tempHtml = f.read()
        f.close()
    with open(full_path + "/example.css","r") as g:
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
        with open(output_path + "workaround-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_json)

if __name__ == "__main__":
    html_css_work_around(api_key, users_guide_resource_path, output_path + "/users-guide-output/")