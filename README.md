# Libellum

Tiny script to generate invoices for independent contractors leveraging wkhtmltopdf.
This script was only tested with Python 3. The payment QR it includes complies with the SEPA Credit Transfer guidelines established by the [European Payments Council](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2018-05/EPC069-12%20v2.1%20Quick%20Response%20Code%20-%20Guidelines%20to%20Enable%20the%20Data%20Capture%20for%20the%20Initiation%20of%20a%20SCT.pdf).

## Installation

1. Download [wkhtmltopdf binaries](https://wkhtmltopdf.org/downloads.html) and add it to your path
2. Clone/download this repository
3. Install the required python packages, i.e.

```
pip3 install qrcode[pil]
pip3 install pdfkit
```
    
4. Fill in the information pertaining to the invoice you want to create in main.py
5. Execute the script which will generate a pdf called invoice.pdf

## Customizing

Adapt `template.html` and `style.css` to your needs, keeping in mind that wkhtmltopdf can be fickle with recent CSS since it does not yet use the latest version of Qt WebKit. You can add more fields in the template by adding them both in the details dictionary in `main.py` as well as referring them in `template.html`.

## Example output

<img src="/example.jpg" alt="Example output" width="600">

## Future plans

- [ ] Add different themes
- [ ] Add a possibility to add different lines pertaining to different tasks
- [ ] Add a possibility to customize the number of columns + their title
- [ ] Make SEPA Credit Transfer QR optional
- [ ] Add possibility to add a company logo
