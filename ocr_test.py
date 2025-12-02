import cv2
import pytesseract

img = cv2.imread('test_image_2.jpg')
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

print(text)
