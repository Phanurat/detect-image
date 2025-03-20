import cv2
import numpy as np

# โหลดรูปภาพโพสต์ Facebook
image = cv2.imread("image/test1.png")
template = cv2.imread("image/like_buttom.png")

# ตรวจสอบว่าโหลดไฟล์ได้หรือไม่
if image is None or template is None:
    print("❌ ไม่สามารถโหลดไฟล์ test.png หรือ like_buttom.png")
    exit()

# แปลงภาพทั้งหมดเป็น Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# ใช้ Template Matching หา Like Button
result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

# ตรวจสอบผลลัพธ์
print("Max Match Value:", np.max(result))  # แสดงค่าแม็กซ์ของการจับคู่

# หาตำแหน่งที่ตรงกับ Template
threshold = 0.5  # ลด threshold เป็น 0.5
loc = np.where(result >= threshold)

# ตรวจสอบว่ามีตำแหน่งที่ตรงกับผลลัพธ์ไหม
if len(loc[0]) == 0:
    print("❌ ไม่พบการจับคู่ที่เหมาะสม!")
else:
    # แสดงตำแหน่งที่พบปุ่ม Like ด้วยกรอบสีเขียว
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 3)  # กรอบสีเขียว

        # แสดงตำแหน่งของกรอบ
        print("Detected at:", pt)

    # แสดงผลภาพ
    cv2.imshow("Detected Like Button", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
