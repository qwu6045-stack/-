from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-pose.pt")
cv2.namedWindow('YOLOv8 Pose',cv2.WINDOW_NORMAL) 
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32

screen_width = user32.GetSystemMetrics(0)  # 屏幕宽度
screen_height = user32.GetSystemMetrics(1) # 屏幕高度

#print(f"屏幕：宽={screen_width} 高={screen_height}")
cv2.resizeWindow('YOLOv8 Pose',screen_width,screen_height)

# 0代表电脑默认摄像头
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_EXPOSURE,-6)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 推理，conf置信度阈值
    results = model(cv2.flip(frame,1), conf=0.7)

    # 绘制结果
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Pose", annotated_frame)

    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()