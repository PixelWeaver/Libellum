import pdfkit
import qrcode
import os
import shutil
import codecs


details = {
    # Company information
    'cpnName': "John Doe",
    'cpnAddrLine1': "Rue de la Frite",
    'cpnAddrLine2': "6969 Aubel",
    'cpnAddrLine3': "Belgium",
    'cpnEmail': "john@doe.beer",
    'cpnPhone': "+69 420 911 666",
    'cpnVat': "11-11-11",

    # Client information
    'cltName': "Voodoo Belgium",
    'cltAddrLine1': "Chaussée des Gascons, 69",
    'cltAddrLine2': "6969 Hasselt",
    'cltAddrLine3': "Belgium",

    # Invoice information
    'invoiceNumber': "2021-01",
    'invoiceDate': "28/07/21",
    'invoicePeriod': "05/07/21 - 28/07/21",
    'position': "Developer",
    'workdays': 20,
    'rate': 745,
    'vatRate': 6,

    # Payment information
    'iban': "BE69 0644 3454 1307",
    'bic': "GKCCBEBB",
    'currency': "EUR",
}

# Calculated fields
details['subtotal'] = details['workdays'] * details['rate']
details['computedVat'] = (details['vatRate'] / 100) * details['subtotal']
details['total'] = details['subtotal'] + details['computedVat']
details['communication'] = f"Payslip - {details['cpnName']} - July 2021",

# Empty cache and ensure directory existence
if os.path.isdir("cache"):
    for root, dirs, files in os.walk("cache"):
        for file in files:
            os.remove(os.path.join(root, file))
else:
    os.mkdir("cache")

# Generate SCT QR code
sct_string = f'BCD\n002\n1\nSCT\n{details["bic"]}\n{details["cpnName"]}\n{details["iban"].replace(" ", "")}\n{details["currency"]}{details["total"]}\n\n\n{details["communication"]}\n' # See SEPA Credit Transfer (SCT) guidelines published at https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2018-05/EPC069-12%20v2.1%20Quick%20Response%20Code%20-%20Guidelines%20to%20Enable%20the%20Data%20Capture%20for%20the%20Initiation%20of%20a%20SCT.pdf
qrcode.make(sct_string).save("cache/payqr.jpg") # Had to use non-vectorial format because issues with svg and wkhtmltopdf

# Load template and fill relevant fields
with open("template.html", "r") as input:
    template = input.read()
    with codecs.open("cache/output.html", "w", "utf8") as output:
        for key, value in details.items():
            template = template.replace(f"${key}", f"{value}")
        output.write(template)
shutil.copyfile("style.css", "cache/style.css")

# Generate PDF
pdfkit.from_file('cache/output.html', 'invoice.pdf', {
    'page-size': 'A4',
    'encoding': "UTF-8",
    'enable-local-file-access': ''
})

