import qrcode

# Use your live GitHub Pages link
# This URL will now trigger the direct PDF view we set up
url = "https://samriddhigroupssince2014.github.io/MOMOAMMORE_MENU/"

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("Samriddhi_Menu_QR.png")

print("QR Code generated successfully!")