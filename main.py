import pdfkit
import qrcode

workdays = 3
rate = 235
vat = 6
name = "Antoine Cajot"
iban = "BE29063534715464"
bic = "GKCCBEBB"
amount = (workdays * rate) * (1 + vat / 100)
currency = "EUR"
communication = "Payslip"

sct_string = f'BCD\n002\n1\nSCT\n{bic}\n{name}\n{iban}\n{currency}{amount}\n\n\n{communication}\n'
img = qrcode.make(sct_string)
img.save("payqr.jpg")

options = {
    'page-size': 'A4',
    'encoding': "UTF-8",
    'enable-local-file-access': ''
}

pdfkit.from_file('template.html', 'out.pdf', options)

