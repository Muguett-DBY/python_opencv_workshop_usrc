import cv2

# reading images
img = cv2.imread('Photos/Sanji.jpg')
cv2.imshow('Ori', img)

scale = 0.5
width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)
dimensions = (width, height)
img0 = cv2.resize(img, (width, height))

cv2.imshow('Resized', img0)

lined = cv2.line(img0, (0, 0), (250, 250), (255, 255, 0), thickness=2)
cv2.imshow('Line', lined)

greyscale = cv2.cvtColor(lined, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscale', greyscale)

blur = cv2.GaussianBlur(greyscale, (9, 9), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

canny = cv2.Canny(blur, 125, 200)
cv2.imshow('Canny Layer', canny)

rotPoint = (width // 2, height // 2)
rotMat = cv2.getRotationMatrix2D(rotPoint, 45, scale=1.0)

rotate = cv2.warpAffine(canny, rotMat, dimensions)
cv2.imshow('Rotated', rotate)

cv2.waitKey(0)
