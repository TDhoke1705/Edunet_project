Simple steganography technique to hide secret messages within images by modifying pixel values based on ASCII mappings. It also includes a password-protected decryption process to retrieve hidden messages.

Features
Hide Secret Messages: Embed secret messages within an image using pixel manipulation.

Password Protection: Ensure restricted access to hidden messages with password-protected decryption.

Simple Implementation: Lightweight and easy-to-understand code using Python.

Image Format Support: Works with any image format supported by OpenCV.

Technologies Used
Python: Programming language

OpenCV (cv2): Image processing and manipulation

OS Module: Handling system operations

Installation & Usage
Prerequisites
Make sure you have Python 3.x installed along with the required libraries:

bash
pip install opencv-python
How to Run
Clone this repository:

bash
git clone https://github.com/your-username/steganography.git
cd steganography
Place your image inside the project folder and update the script with its path.

Run the script:

bash
python stego.py
Enter the secret message and a password for encryption. The script generates an encrypted image containing the hidden message.

Run the script again and enter the correct password to decrypt the hidden message.

Limitations & Future Enhancements
No Encryption: Direct ASCII mapping makes it vulnerable to attacks.

Hardcoded Image Path: Needs manual updates for different images.

Basic Pixel Allocation: Can lead to data loss in large messages.

Future Improvements
Implement AES encryption for secure message encoding.

Use randomized pixel mapping to improve security.

Support larger message sizes with optimized storage techniques.

End Users
This project is useful for cybersecurity enthusiasts, students, forensic analysts, and privacy-conscious individuals interested in data hiding techniques.
