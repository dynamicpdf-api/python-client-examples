from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.text_element import TextElement
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.template import Template
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.pdf_input import PdfInput
from dynamicpdf_api.elements.line_element import LineElement
from dynamicpdf_api.elements.rectangle_element import RectangleElement
from dynamicpdf_api.elements.image_element import ImageElement
from dynamicpdf_api.line_style import LineStyle
from dynamicpdf_api.image_resource import ImageResource

from Shared import *

def template_example(apikey, full_path):
    template = Template("TemplateA")
    
    textElement = TextElement("Hello PDF", ElementPlacement.TopCenter, 50, 100)
    textElement.color = RgbColor.blue()
    textElement.font_size = 42
    textElement.x_offset = -50
    textElement.y_offset = 100

    element = LineElement(ElementPlacement.TopLeft, 100, 100)
    element._color = RgbColor.red()
    element.x_offset = 125
    element.y_offset = 150
    element.x2_offset = 450
    element.y2_offset = 150
    element.line_style = LineStyle.solid()
    element.width = 4

    recElement = RectangleElement(ElementPlacement.TopCenter, 100, 500)
    recElement.x_offset = -250
    recElement.y_offset = 50
    recElement.corner_radius = 10
    recElement.border_width = 5
    recElement.border_style = LineStyle.dots()
    recElement.border_color = RgbColor.blue()
    recElement.fill_color = RgbColor.green()

    imgResource = ImageResource(full_path + "dynamicpdfLogo.png")
    imageElement = ImageElement(imgResource, ElementPlacement.TopCenter, 100, 80)

    template.elements.append(textElement)
    template.elements.append(element)
    template.elements.append(recElement)
    template.elements.append(imageElement)

    pdf=Pdf()
    pdf.api_key = apikey
    resource = PdfResource(full_path + "DocumentA.pdf")
    input = PdfInput(resource)
    input.template = template
    pdf.inputs.append(input)

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "template-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    template_example(api_key, base_path + "/templates/")