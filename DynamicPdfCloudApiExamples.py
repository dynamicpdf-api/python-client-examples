
import shutil
import os
from pathlib import Path
from AddBookmarks import bookmark_pdf
from ExcelExample import excel_example
from ImageInfoExample import image_info
from MergeSolution import merge_solution
from PdfBarcode import pdfbarcode_example
from PdfXmpExample import pdf_xmp_info
from CompletingAcroform import completing_acroform
from CreatePdfDlex import create_pdf_dlex
from DlexLayoutExample import dlex_layout
from MergePdfs import merge_pdfs
from GoogleFontExample import google_example
from PdfDlexExample import pdf_dlex_example
from PdfExample import pdf_example
from PdfHtmlCssWorkAroundExample import html_css_work_around
from PdfHtmlExample import html_example
from PdfInfoExample import pdf_info_example
from PdfTextExample import pdf_text_example
from InstructionsExample import instruction_example
from SolutionImagesTextRecs import solutionsImageTextRecs_example
from ImageConversion import image_conversion_example
from TemplateExample import template_example
from OutlinesSolution import outlines_solution
from DeletePages import delete_pages
from SplitPdf import split_pdf
from FormFieldFlattenDelete import form_field_flatten_delete
from WordExample import word_example

from Shared import *

def copy_folder():
    if not os.path.exists("./output"):
        os.makedirs("./output")

def run():
    copy_folder()

    bookmark_pdf(api_key, base_path + "/add-bookmarks/")
    completing_acroform(api_key)
    create_pdf_dlex(api_key, base_path + "/creating-pdf-pdf-endpoint/")
    delete_pages(api_key, base_path + "/delete-pages/")
    dlex_layout(api_key, base_path + "/creating-pdf-dlex-layout/")
    excel_example(api_key, "./resources/users-guide/", "./output/")
    form_field_flatten_delete(api_key, base_path + "/form-field-flatten/")
    google_example(api_key)
    html_example(api_key, base_path + "/users-guide/")
    html_css_work_around(api_key,  base_path + "/users-guide/")
    image_conversion_example(api_key, base_path + "/image-conversion/")
    image_info(api_key, base_path + "/image-info/")
    instruction_example(api_key, base_path + "/users-guide/") 
    merge_pdfs(api_key, base_path + "/merge-pdfs-pdf-endpoint/")
    merge_solution(api_key, base_path, output_path)
    outlines_solution(api_key, base_path + "/outlines/")
    pdf_example(api_key)
    pdfbarcode_example(api_key)
    pdf_dlex_example(api_key, base_path + "/creating-pdf-pdf-endpoint/")
    pdf_info_example(api_key, base_path + "/get-pdf-info-pdf-info-endpoint/")
    pdf_text_example(api_key, base_path + "/pdf-info/")
    pdf_xmp_info(api_key, base_path + "/get-xmp-metadata-pdf-xmp-endpoint/")
    solutionsImageTextRecs_example(api_key, base_path + "/images-text-recs/")
    split_pdf(api_key, base_path + "/split-pdf/")
    template_example(api_key, base_path + "/templates/")
    word_example(api_key, "./resources/users-guide/", "./output/")     

    
if __name__ == "__main__":
    run()