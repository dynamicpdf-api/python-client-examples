
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
from PdfDlexExample import pdf_dlex_example
from PdfExample import pdf_example
from PdfHtmlCssWorkAroundExample import html_css_work_around
from PdfHtmlExample import html_example
from PdfInfoExample import pdf_info_example
from PdfTextExample import pdf_text_example
from InstructionsExample import instruction_example
from Shared import api_key
from Shared import base_path

def copy_folder():
    if not os.path.exists("./output"):
        os.makedirs("./output")

def run():
    copy_folder()
    bookmark_pdf(api_key, base_path + "/add-bookmarks/")
    image_info(api_key, base_path + "/image-info/")
    pdf_xmp_info(api_key, base_path + "/get-xmp-metadata-pdf-xmp-endpoint/")
    completing_acroform(api_key, base_path + "/fill-acro-form-pdf-endpoint/")
    create_pdf_dlex(api_key, base_path + "/creating-pdf-pdf-endpoint/")
    dlex_layout(api_key, base_path + "/dlex-layout/")
    merge_pdfs(api_key, base_path + "/merge-pdfs-pdf-endpoint/")
    pdf_dlex_example(api_key, base_path + "/creating-pdf-pdf-endpoint/")
    pdf_example(api_key, base_path + "/pdf-example/")
    html_css_work_around(api_key, base_path + "/users-guide/")
    html_example(api_key, base_path + "/pdf-html-example/")
    pdf_info_example(api_key, base_path + "/pdf-info/")
    pdf_text_example(api_key, base_path + "/pdf-info/")
    instruction_example(api_key, base_path + "/users-guide/") 

if __name__ == "__main__":
    run()