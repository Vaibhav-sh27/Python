import cv2
img_location="v.jpg"
#file_name='v.jpg'
img=cv2.imread(img_location)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_img=255-gray_image
blurr_img=cv2.GaussianBlur(inverted_gray_img,(21,21),0)
inverted_blurr_img=255-blurr_img
pencil_sketch_img=cv2.divide(gray_image,inverted_blurr_img,scale=246.0)
cv2.imshow('Original img',img)
cv2.imshow('New img',pencil_sketch_img)

cv2.waitKey(0)