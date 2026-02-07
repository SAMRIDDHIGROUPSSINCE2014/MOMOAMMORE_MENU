import qrcode
import os

# 1. YOUR INTERACTIVE SITE URL
# Removing 'menu.pdf' ensures the QR code opens your index.html gallery
url = "https://samriddhigroupssince2014.github.io/MOMOAMMORE_MENU/"

# 2. QR CODE CONFIGURATION
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction for restaurant use
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# 3. GENERATE AND SAVE
# Creating a distinct filename to avoid confusion with previous versions
img_name = "MomoAmore_Interactive_QR.png"
img = qr.make_image(fill_color="black", back_color="white")
img.save(img_name)

print(f"Success! QR code linked to {url} has been saved as {img_name}")