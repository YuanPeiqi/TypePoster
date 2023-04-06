import cv2
import numpy as np

def vertical_grad(src,color_start,color_end):
    h = src.shape[0]

    # 创建一幅与原图片一样大小的透明图片
    grad_img = np.ndarray(src.shape,dtype=np.uint8)

    # opencv 默认采用 BGR 格式而非 RGB 格式
    g_b = float(color_end[0] - color_start[0]) / h
    g_g = float(color_end[1] - color_start[1]) / h
    g_r = float(color_end[2] - color_start[2]) / h

    for i in range(h):
        for j in range(src.shape[1]):
            grad_img[i,j,0] = color_start[0] + i * g_b
            grad_img[i,j,1] = color_start[1] + i * g_g
            grad_img[i,j,2] = color_start[2] + i * g_r

    return grad_img


if __name__ == '__main__':
    img = cv2.imread('E:\\project\\TypePoster\\poster_backend\\static\\backgrounds\\test_user\\cs_1.png')
    grad_img = vertical_grad(img,(255,255,255),(0,0,0))
    blend = cv2.addWeighted(img, 1.0, grad_img, 0.6, 0.0)
    cv2.imshow('img', grad_img)
    cv2.imshow('gradients',blend)
    cv2.imwrite('E:\\project\\TypePoster\\poster_backend\\static\\backgrounds\\test_user\\test.png', blend)
