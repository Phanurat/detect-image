from yolov5 import YOLOv5

model = YOLOv5("yolov5s.pt")  # ดาวน์โหลดโมเดล YOLOv5 จาก repository
result = model.predict("image/test5.png")  # ส่งภาพให้โมเดลตรวจจับ
result.show()  # แสดงผลลัพธ์
