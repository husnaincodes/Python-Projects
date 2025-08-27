import qrcode
data = input("Enter Your URL Please : ").strip()
filename = input("Enter Your File Name : ").strip()
qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color= "black",back_color = "white")
image.save(filename)
print(f"QR code save as {filename}")