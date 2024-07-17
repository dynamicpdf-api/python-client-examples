![](./logo-banner2.png)

# python-client-examples

The DynamicPDF API Client Examples uses the DynamicPDF API Python client library (`python-client`) to create, merge, split, form fill, stamp, obtain metadata, convert, and secure/encrypt PDF documents. This project contains numerous sample projects for the tutorials and examples on [dpdf.io](https://dpdf.io/).

The DynamicPDF API consists of the following endpoints.

- `dlex-layout`
- `image-info`
- `pdf`
- `pdf-info`
- `pdf-text`
- `pdf-xmp`

The Python client library (`python-client`) is available on Github ([python-client]([https://github.com/dynamicpdf-api/python-client](https://github.com/dynamicpdf-api/python-client))). For more information, please visit [DynamicPDF Cloud API](https://cloud.dynamicpdf.com/). Support for other languages/platforms (Java, PHP, C#, Node.js, Python) is available on GitHub ([DynamicPDF API at GitHub](https://github.com/dynamicpdf-api)).

## PyPI Package
Obtain the PyPI package at https://pypi.org/project/dynamicpdf-api/

## Running
To run any example, set your DynamicPDF API api key in the Shared.py file.
Run an individual file by typing python -filename-.py
Run all the files at once by running the DynamicPdfCloudApiExamples.py file.

**Be certain to have added the needed samples in your cloud storage before running.**

If running all at once, you need the following samples in your cloud storage.
* samples/creating-pdf-pdf-endpoint/
* samples/fill-acro-form-pdf-endpoint/
* samples/image-info/
* samples/creating-pdf-dlex-layout-endpoint/
* samples/merge-pdfs-pdf-endpoint/
* samples/blog-dynamic-columns/


## Resources

The local resources for this project are in the project's resources folder.

- [File Manager Samples](https://cloud.dynamicpdf.com/docs/usersguide/environment-manager/environment-manager-sample-resources)  

Some examples require you have the sample project in your DynamicPDF API File Manager. 

* For example, samples/creating-pdf-dlex-layout-endpoint/creating-pdf-dlex-layout.dlex is a resource in the samples/creating-pdf-dlex-layout-endpoint folder in your file manager.  See the document for more information on adding samples to your cloud storage space.

Local files are in the resources folder, and the examples output to the output folder (which is created when run).

For more information on the tutorials and example code, refer to:

- https://cloud.dynamicpdf.com/docs/tutorials/tutorials-overview
- https://cloud.dynamicpdf.com/docs/usersguide/cloud-api/cloud-api-overview

## **Tutorials**

The following table lists the available tutorials.

| Tutorial Title                                     | Project/File/Class      | Tutorial Location                                            |
| -------------------------------------------------- | ----------------------- | ------------------------------------------------------------ |
| Merging PDFs                                       | `MergePdfs.py`               | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/merging-pdfs |
| Completing an AcroForm                             | `CompletingAcroform.py`    | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/form-completion |
| Creating a PDF Using a DLEX and the `pdf` Endpoint | `CreatePdfDlex.py`       | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/dlex-pdf-endpoint |
| Adding Bookmarks to a PDF                          | `AddBookmarks.py`          | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/bookmarks |
| Creating a PDF Using the `dlex-layout` Endpoint    | `DlexLayoutExample.py` | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/dlex-layout |
| Extracting Image Metadata                          | `ImageInfoExample.py`          | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/image-info |
| Extract PDF Metadata                               | `PdfInfoExample.py`            | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/pdf-info |
| Extracting PDF's Text                              | `PdfTextExample.py`        | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/pdf-text |
| Extract XMP Metadata                               | `PdfXmpExample.py        | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/pdf-xmp |
| Convert HTML to PDF                                | `PdfHtmlExample.py`   | https://cloud.dynamicpdf.com/docs/tutorials/cloud-api/pdf-html |

# Support

The primary source for the DynamicPDF API support is through [Stack Overflow](https://stackoverflow.com/questions/tagged/dynamicpdf-api). Please use the "[dynamicpdf-api](https://stackoverflow.com/questions/tagged/dynamicpdf-api)" tag to ask questions. Our support team actively monitors the tag and responds promptly to any questions.  Also, let us know you asked the question by following up with an email to [support@dynamicpdf.com](mailto:support@dynamicpdf.com). 

## Pro Plan Subscribers[#](https://cloud.dynamicpdf.com/support#pro-plan-subscribers)

Ticket support is available to Pro Plan subscribers. But we still encourage you to help the community by posting on Stack Overflow when possible. You can also email [support@dynamicpdf.com](mailto:support@dynamicpdf.com) if you need to ask something specific to your use case that may not help the DynamicPDF API community.

# License

The `dotnet-client-examples` library is licensed under the [MIT License](./LICENSE).
