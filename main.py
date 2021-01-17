import qrcode

img = qrcode.make('Hello World')
img.save('Hello.png')
# advanced

qr = qrcode.QRCode(
    version=1,
    box_size=22,
    border=5

)

qr.add_data('https://github.com/Rabin321')
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('Github link.png')