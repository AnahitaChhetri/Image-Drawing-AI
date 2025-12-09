import cv2
import numpy as np

image=np.zeros((500, 500, 3),dtype="uint8")
text="Shapes"
font=cv2.FONT_HERSHEY_SIMPLEX
scale=1
thickness=1
(text_width, text_height), baseline=cv2.getTextSize(text, font, scale, thickness)

image_width=image.shape[1]
x=(image_width - text_height)//2
y=text_height+20
cv2.putText(image, text, (x,y), font, scale, (0,255,255), 2, cv2.LINE_AA)
cv2.imshow("Shapes",image)
cv2.line(image, (50,50), (450,50),(0,0,255), 3)
cv2.circle(image, (250,200), 80, (255, 0, 0),3)
cv2.rectangle(image,(100,300), (400,450), (0,250,0), 3)
cv2.rectangle(image, (50,300), (150,400), (255,255,0), 3)
cv2.arrowedLine(image, (200,100),(300,100), (255,255,0), 3)

cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()