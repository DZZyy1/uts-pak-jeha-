import cv2
import numpy as np
import os


os.makedirs("output", exist_ok=True)

canvas = np.full((400, 400, 3), 255, dtype=np.uint8)

cv2.rectangle(canvas, (100, 250), (300, 300), (100, 100, 100), -1) 
cv2.rectangle(canvas, (140, 200), (260, 250), (120, 120, 120), -1)  
cv2.rectangle(canvas, (260, 215), (340, 230), (80, 80, 80), -1) 
for x in range(120, 281, 40):
    cv2.circle(canvas, (x, 310), 15, (0, 0, 0), -1) 
    cv2.circle(canvas, (x, 310), 6, (150, 150, 150), -1)  
cv2.circle(canvas, (200, 225), 8, (0, 0, 0), -1)
cv2.line(canvas, (200, 200), (200, 160), (0, 0, 0), 3)
cv2.circle(canvas, (200, 155), 5, (0, 0, 255), -1)

cv2.imwrite("output/tank.png", canvas)
print("Gambar tank berhasil disimpan di folder output/")

cropped = canvas[100:300, 100:300]
cv2.imwrite("output/crop.png", cropped)
