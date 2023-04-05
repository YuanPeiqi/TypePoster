import cv2
import numpy as np
bg_img = cv2.imread("C:\\Users\\Administrator\\Desktop\\db.png", cv2.IMREAD_UNCHANGED)
a = np.full(fill_value=255, shape=bg_img.shape, dtype=np.uint8)
a = cv2.addWeighted(bg_img, 0.5, a, 0.5, 1)
cv2.imwrite('C:\\Users\\Administrator\\Desktop\\db2.png', a)
