import cv2



img = cv2.imread(r"C:\Users\Tanmay\Downloads\edunet project\mypic.jpg")
import os

image_path = r"C:\Users\Tanmay\Downloads\edunet project\mypic.jpg"

if not os.path.exists(image_path):
    print("Error: The specified image file does not exist!")
else:
    print("Image file found successfully.")
# Replace with the correct image path#image

msg = input("Enter the secret message which you want to hide:")
password = input("Enter a password to protect file:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[int(img[n, m, z])]

        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
