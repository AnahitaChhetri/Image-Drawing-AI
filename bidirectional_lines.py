import cv2
import numpy as np

image=np.zeros((500, 800, 3), dtype="uint8")
text="Bidirectional Arrows"
font=cv2.FONT_HERSHEY_SIMPLEX
scale=1
thickness=1
text_width, text_height=cv2.getTextSize(text,font,scale,thickness)

image_width=image.shape[1]
text_x=(image_width-text_height)//2
text_y=text_height+20
cv2.putText(image, text, (text_x,text_y), font, scale, (0,255,255), 2, cv2.LINE_AA)


cv2.arrowedLine(image, (800,450),(100,450), (255,255,0), 3)
cv2.arrowedLine(image, (100,50), (800, 50), (255, 255,0), 3)

cv2.imshow("Arrows:", image)
cv2.waitKey(0)
cv2.destroyAllWindows()