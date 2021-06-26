
import pyqrcode

msg = "salman"

QR = pyqrcode.create(msg)
QR.png("QR.png", scale = 20)