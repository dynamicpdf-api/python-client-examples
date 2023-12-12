![](./logo-banner2.png)

# python-client-examples

The Cloud API Client Examples uses the DynamicPDF Cloud API Go client library (`go-client`) to create, merge, split, form fill, stamp, obtain metadata, convert, and secure/encrypt PDF documents. This project contains numerous sample projects for the tutorials and examples on [cloud.dynamicpdf.com](https://cloud.dynamicpdf.com/).

The DynamicPDF Cloud API consists of the following endpoints.

- `dlex-layout`
- `image-info`
- `pdf`
- `pdf-info`
- `pdf-text`
- `pdf-xmp`

The Python client library (`go-client`) is available on Github ([python-client]([https://github.com/dynamicpdf-api/go-client](https://github.com/dynamicpdf-api/python-client))). For more information, please visit [DynamicPDF Cloud API](https://cloud.dynamicpdf.com/). Support for other languages/platforms (Java, PHP, C#, Node.js, Python) is available on GitHub ([DynamicPDF Cloud API at GitHub](https://github.com/dynamicpdf-api)).

## PyPI Package
Obtain the PyPI package at https://pypi.org/project/dynamicpdf-api/


## Resources

The local resources for this project are in the project's resources folder.

- [Resource Manager Samples](https://cloud.dynamicpdf.com/docs/usersguide/environment-manager/environment-manager-sample-resources)  

You need the following samples folder in your Cloud Storage space to run all the examples.

* samples/report-with-cover-page
* samples/creating-pdf-pdf-endpoint
* samples/creating-a-report-template-designer
* samples/creating-a-page-template-designer
* samples/dlex-layout
* samples/merge-pdfs-pdf-endpoint
* samples/fill-acro-form-pdf-endpoint
* samples/creating-a-page-template-designer

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

The primary source for the DynamicPDF Cloud API support is through [Stack Overflow](https://stackoverflow.com/questions/tagged/dynamicpdf-api). Please use the "[dynamicpdf-api](https://stackoverflow.com/questions/tagged/dynamicpdf-api)" tag to ask questions. Our support team actively monitors the tag and responds promptly to any questions.  Also, let us know you asked the question by following up with an email to [support@dynamicpdf.com](mailto:support@dynamicpdf.com). 

## Pro Plan Subscribers[#](https://cloud.dynamicpdf.com/support#pro-plan-subscribers)

Ticket support is available to Pro Plan subscribers. But we still encourage you to help the community by posting on Stack Overflow when possible. You can also email [support@dynamicpdf.com](mailto:support@dynamicpdf.com) if you need to ask something specific to your use case that may not help the DynamicPDF Cloud API community.

# License

The `dotnet-client-examples` library is licensed under the [MIT License](./LICENSE).
