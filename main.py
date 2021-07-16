import pdfkit
import qrcode

iban = "BE29 0635 3471 5494"
amount = 747
currency = "EUR"
communication = "Payslip - Antoine Cajot - July"

img = qrcode.make(f'SPD*1.0*ACC:{iban}*AM:{amount}*CC:{currency}*MSG:{communication}')
img.save("payqr.svg")

options = {
    'page-size': 'A4',
    'encoding': "UTF-8",
    'enable-local-file-access': ''
}

pdfkit.from_file('template.html', 'out.pdf', options)

