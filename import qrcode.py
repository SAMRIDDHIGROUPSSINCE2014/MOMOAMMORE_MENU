import qrcode

# 1. Your actual live GitHub URL
# Replace this with your exact GitHub Pages link
url = "https://samriddhigroupssince2014.github.io/MOMOAMMORE_MENU/"

# 2. Configure the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction for printing
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# 3. Create and save the image
# You can change 'black' to 'chocolate' or 'darkorange' for a bakery vibe!
img = qr.make_image(fill_color="black", back_color="white")
img.save("1QR.png")

print("Success! Your QR code is saved as 1QR.png")