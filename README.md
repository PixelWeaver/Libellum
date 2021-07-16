# Libellum

Minimal script to generate invoices for independent contractors leveraging wkhtmltopdf

## Installation

1. Download [wkhtmltopdf binaries](https://wkhtmltopdf.org/downloads.html) and add it to your path
2. Clone/download this repository
3. Install the required python packages, i.e.

    `pip3 install qrcode[pil]`
    `pip3 install pdfkit`
    
4. Fill in the information pertaining to the invoice you want to create in main.py
5. Execute the script which will generate a pdf called invoice.pdf

## Customizing

Adapt template.html and style.css to your needs, keeping in mind that wkhtmltopdf can be fickle with recent CSS since it does not yet use the latest version of Qt WebKit.

## Future plans

- [ ] Add different themes
- [ ] Add a possibility to add different lines pertaining to different tasks
- [ ] Make SEPA Credit Transfer QR optional
- [ ] Add possibility to add a company logo

## Example output
