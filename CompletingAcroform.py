from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.pdf_resource import PdfResource
from dynamicpdf_api.form_field import FormField

def completing_acroform(apiKey, basePath):
    
    pdf=Pdf()
    pdf.api_key=apiKey
    pdf.add_pdf(PdfResource(basePath + "fw9AcroForm_18.pdf"))

    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].f1_1[0]", "Any Company, Inc."))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].f1_2[0]", "Any Company"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].FederalClassification[0].c1_1[0]", "1"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].Address[0].f1_7[0]", "123 Main Street"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].Address[0].f1_8[0]", "Washington, DC  22222"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].f1_9[0]", "Any Requester"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].f1_10[0]", "17288825617"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].EmployerID[0].f1_14[0]", "52"))
    pdf.form_fields.append(FormField("topmostSubform[0].Page1[0].EmployerID[0].f1_15[0]", "1234567"))
      
    response = pdf.process() 
    if response.is_successful:
         with open(basePath + "form-fill-output-python.pdf", "wb") as file:
            file.write(response.content)
    else:
        print(response.error_id)
    
# Call the function
api_key = 'DP.25DHurNAMB8MEgzPg3mmUyBsjkqQbjgVAZuFuu4ynh6OSaBCOp6JIrR7'
completing_acroform(api_key, "C:/temp/dynamicpdf-api-samples/")