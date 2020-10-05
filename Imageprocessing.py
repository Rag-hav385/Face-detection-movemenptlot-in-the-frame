import cv2
import glob

'''

img = cv2.imread("galaxy.jpg",0) #0 > black n white 1 > colour

resized_img = cv2.resize(img,(200,200)) #resixing image
cv2.imshow("Galaxy",img)#showing image

#To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

#to write in other file
#cv2.imwrite("filename.jpg",variable)

'''

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image,0)
    re = cv2.resize(img,(100,100))
    cv2.imshow("Hey" , re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resizes" + image,re)


