from dynamicpdf_api.pdf import Pdf
from dynamicpdf_api.word_resource import WordResource
from Shared import *

def word_example(apikey, documentPath, outputPath):
    
    pdf=Pdf()
    pdf.api_key=apikey
    pdf.add_word(WordResource(documentPath + "Doc1.docx"))
    
    response = pdf.process() 

    if response.is_successful:
         with open(output_path + "pdf-word-output-python.pdf", "wb") as output_file:
            output_file.write(response.content)
    else:
        print(response.error_id)
    
if __name__ == "__main__":
    word_example(api_key, "./resources/users-guide/", "./output/")