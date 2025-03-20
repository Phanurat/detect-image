import cv2
import os

# ตรวจสอบว่าภาพมีอยู่จริง
image_path = "image/test.jpg"
template_path = "image/like_button.png"

print("Image exists:", os.path.exists(image_path))
print("Template exists:", os.path.exists(template_path))

# ลองโหลดภาพ
image = cv2.imread(image_path)
template = cv2.imread(template_path)

if image is None:
    print("❌ ไม่สามารถโหลด image/test.jpg")
if template is None:
    print("❌ ไม่สามารถโหลด image/like_button.png")
