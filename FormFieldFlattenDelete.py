from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.form_field import FormField
from dynamicpdf_api.pdf_input import PdfInput
from Shared import *

def form_field_flatten_delete(apikey, full_path):
    
    pdf=Pdf()
    pdf.api_key = apikey
    
    resource = PdfResource(full_path + "fw9AcroForm_14.pdf", "fw9AcroForm_14.pdf")
    input = PdfInput(resource)
    pdf.inputs.append(input)

    field = FormField("topmostSubform[0].Page1[0].f1_1[0]", "Any Company, Inc.")
    field.flatten = True
    pdf.form_fields.append(field)
    field1 = FormField("topmostSubform[0].Page1[0].f1_2[0]", "Any Company")
    field1.remove = True
    pdf.form_fields.append(field1)
    field2 = FormField("topmostSubform[0].Page1[0].FederalClassification[0].c1_1[0]", "1")
    field2.flatten = True
    pdf.form_fields.append(field2)
    field3 = FormField("topmostSubform[0].Page1[0].Address[0].f1_7[0]", "123 Main Street")
    field3.Flatten = False
    pdf.form_fields.append(field3)
    field4 = FormField("topmostSubform[0].Page1[0].Address[0].f1_8[0]", "Washington, DC  22222")
    field4.flatten = False
    pdf.form_fields.append(field4)
    field5 = FormField("topmostSubform[0].Page1[0].f1_9[0]", "Any Requester")
    field5.remove = True
    
    pdf.form_fields.append(field5)

    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "form-flatten-delete-output-python.pdf", "wb") as file:
            file.write(response.content)
    else:
        print(response.error_id)

if __name__ == "__main__":
    form_field_flatten_delete(api_key, base_path + "/form-field-flatten/")