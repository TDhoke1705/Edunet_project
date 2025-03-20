import cv2
import os

# Load image correctly
image_path = r"C:\Users\Tanmay\Downloads\32822.jpg"

if not os.path.exists(image_path):
    print("Error: The specified image file does not exist!")
    exit()

img = cv2.imread(image_path)

# Ensure the image is loaded correctly
if img is None:
    print("Error: Could not read the image.")
    exit()
else:
    print("Image file found successfully.")

# Take message input
msg = input("Enter the secret message which you want to hide: ")
password = input("Enter a password to protect file: ")

# Dictionaries for encoding/decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Message encoding into image
m, n, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Store ASCII value in the pixel
    m += 1  # Move to next pixel
    if m >= img.shape[1]:  # Move to next row if needed
        m = 0
        n += 1

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Message hidden successfully in 'encryptedImage.jpg'.")
os.system("start encryptedImage.jpg")  # Open encrypted image

# Decryption
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[int(img[n, m, z])]  # Retrieve ASCII character
        m += 1
        if m >= img.shape[1]:  # Move to next row if needed
            m = 0
            n += 1
    print("Decrypted message:", message)
else:
    print("ERROR: Incorrect password! Access denied.")
