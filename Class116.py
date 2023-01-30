import cv2

img = cv2.imread("C:/Users/Dell/Desktop/New folder/project/solar-system.jpg")
cv2.putText(img,"Sun",(100,80),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,0,0))
cv2.putText(img,"Mercury",(110,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Venus",(190,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Earth",(300,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Mars",(400,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Jupiter",(500,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Saturn",(720,110),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Uranus",(950,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Neptune",(1080,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))

cv2.imshow("Solar System",img)
cv2.waitKey(0)
cv2.imwrite("Solar_system_withName.jpg",img)