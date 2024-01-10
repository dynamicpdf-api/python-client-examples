from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.rgb_color import RgbColor
from dynamicpdf_api.font import Font
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.text_element import TextElement
from dynamicpdf_api.elements.line_element import LineElement
from dynamicpdf_api.line_style import LineStyle
from dynamicpdf_api.elements.rectangle_element import RectangleElement
from dynamicpdf_api.elements.element_placement import ElementPlacement
from dynamicpdf_api.elements.image_element import ImageElement
from dynamicpdf_api.image_resource import ImageResource
from Shared import *

def solutionsImageTextRecs_example(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key=apikey
    pdf.author = "John Doe"
    pdf.title = "My PDF"
    inputPage = pdf.add_page(1008, 612)
    
    textElement = TextElement("Hello PDF", ElementPlacement.TopCenter, 50, 100)
    textElement.color = RgbColor.blue();
    textElement.font_size = 42;
    textElement.x_offset = -50;
    textElement.y_offset = 100;

    inputPage.elements.append(textElement)

    element = LineElement(ElementPlacement.TopLeft, 200, 200);
    element._color = RgbColor.red();
    element.x_offset = 305;
    element.y_offset = 150;
    element.x2_offset = 900;
    element.y2_offset = 150;
    element.line_style = LineStyle.solid();
    element.width = 4;
    inputPage.elements.append(element);

    recElement = RectangleElement(ElementPlacement.TopCenter, 100, 500);
    recElement.x_offset = -250;
    recElement.y_offset = -10;
    recElement.corner_radius = 10;
    recElement.border_width = 5;
    recElement.border_style = LineStyle.dots();
    recElement.border_color = RgbColor.blue();
    recElement.fill_color = RgbColor.green();
    inputPage.elements.append(recElement);

    imgResource = ImageResource(full_path + "dynamicpdfLogo.png");
    imageElement = ImageElement(imgResource, ElementPlacement.TopCenter, 835, 75);
    inputPage.elements.append(imageElement);

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "solution-images-text-rec-output.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    solutionsImageTextRecs_example(api_key, base_path + "/images-text-recs/")