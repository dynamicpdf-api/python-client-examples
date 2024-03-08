
import shutil
import os
from pathlib import Path
from AddBookmarks import bookmark_pdf
from ImageInfoExample import image_info
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

from Shared import api_key
from Shared import base_path

def copy_folder():
    if not os.path.exists("./output"):
        os.makedirs("./output")

def run():
    copy_folder()
    form_field_flatten_delete(api_key, base_path + "/form-field-flatten/")
    split_pdf(api_key, base_path + "/split-pdf/")
    delete_pages(api_key, base_path + "/delete-pages/")
    outlines_solution(api_key, base_path + "/outlines/")
    template_example(api_key, base_path + "/templates/")
    image_conversion_example(api_key, base_path + "/image-conversion/")
    solutionsImageTextRecs_example(api_key, base_path + "/images-text-recs/")
    bookmark_pdf(api_key, base_path + "/add-bookmarks/")
    image_info(api_key, base_path + "/image-info/")
    pdf_xmp_info(api_key, base_path + "/get-xmp-metadata-pdf-xmp-endpoint/")
    completing_acroform(api_key, base_path + "/fill-acro-form-pdf-endpoint/")
    create_pdf_dlex(api_key, base_path + "/creating-pdf-pdf-endpoint/")
    dlex_layout(api_key, base_path + "/dlex-layout/")
    merge_pdfs(api_key, base_path + "/merge-pdfs-pdf-endpoint/")
    google_example(api_key)
    pdf_dlex_example(api_key, base_path + "/creating-pdf-pdf-endpoint/")
    pdf_example(api_key)
    html_css_work_around(api_key, base_path + "/users-guide/")
    html_example(api_key, base_path + "/users-guide/")
    pdf_info_example(api_key, base_path + "/pdf-info/")
    pdf_text_example(api_key, base_path + "/pdf-info/")
    instruction_example(api_key, base_path + "/users-guide/") 

if __name__ == "__main__":
    run()