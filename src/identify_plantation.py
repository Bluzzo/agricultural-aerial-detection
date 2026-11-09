import cv2
import numpy as np

def analizar_pixel(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        print(f"\nPosición: ({x}, {y})")
        print(f"BGR: {img[y, x]}")
        print(f"HSV: {hsv[y, x]}")
        print(f"Máscara: {mask[y, x]}")


cv2.namedWindow('img')
cv2.setMouseCallback('img', analizar_pixel)

img = cv2.imread('../images/terrain.png')
if img is None:
    raise FileNotFoundError("No se encontro la foto")

h, w = img.shape[:2]
nw = min(w, 1000)
nh = int(h * nw / w)

img = cv2.resize(img, (nw, nh))

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, parcel_mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
parcel_pixels = np.count_nonzero(parcel_mask)


lower_green = np.array([20, 25, 25])
upper_green = np.array([90, 255, 255])


mask = cv2.inRange(hsv, lower_green, upper_green)
vegetation_mask = cv2.bitwise_and(mask,parcel_mask)
vegetation_pixel = np.count_nonzero(vegetation_mask)

if parcel_pixels > 0:
    vegetation_percentage = (vegetation_pixel *100) / parcel_pixels
    print(f'cobertura de vegetacion del {vegetation_percentage:.2f}%')
else:
    print('no se encontro ninguna parcela')


res = cv2.bitwise_and(img,img,mask=vegetation_mask)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
# cv2.imshow('result', res)
cv2.imshow('parcela detectada', parcel_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
