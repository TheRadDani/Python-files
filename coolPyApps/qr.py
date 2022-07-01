import qrcode
import cv2
img = qrcode.make("comame esta, playito")
img.save("qr.jpg")
d = cv2.QRCodeDetector()
retval,points,straight_qrcode = d.detectAndDecode(cv2.imread("qr.jpg"))
print(retval)