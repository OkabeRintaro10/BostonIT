import cv2

#OpenCV app to to live web inferencing and add frames to test folder
cv2.namedWindow("test")

img_counter = 0

while True: 
    ret, frame = cam.read() 
    if not ret:
      print("Failed to grab Frame")
      break 
    cv2.imshow("test",frame)
    k = cv2.waitkey(1)
    if  k%256 == 27:
      print("Close")
      break
    elif k%256 == 32:
      img_name = "test_{}.png".format(img_counter)
      cv2.imwrite(img_name,frame)
      img_counter += 1
    
cam.release()

cam.destroyAllWindows()
