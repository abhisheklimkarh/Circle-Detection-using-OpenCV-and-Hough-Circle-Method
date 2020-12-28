# Import Libraries. 
import cv2 
import numpy as np 
 
# Reading the image.
image = cv2.imread('C:\\Users\\Abhishek Limkar\\Desktop\\Miscos_cv_assignment\\Assignment\\Final Assignment\\images\\coin.jpeg', cv2.IMREAD_COLOR) 

# Converting the image into grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# Now blur the grayscale image using Gaussian Blur.
gray_blurred = cv2.GaussianBlur(gray, (21,21), cv2.IMREAD_UNCHANGED) 
  

# Using Hough Gradient method to detect circles.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1.5, 100, param1=None,
                                    param2=None, minRadius=None, maxRadius=250) 

 
 # Creating 'xcord', 'ycord', and 'rad' lists to store the X, Y, co-ordinates and radius of detected circles.
xcord = []
ycord = []
rad = []
i = 0


if detected_circles is not None: 
    
    # Creating an integer array to read co-ordinates.
    detected_circles = np.round(detected_circles[0, :]).astype('int') 
    
    # Appending co-ordinates to their corresponding lists.
    for (x, y, r) in detected_circles:
        #Printing the values of X, Y cordinates and Radius of the detected circle.
        print('x-cord: ' + str(x) + ' y-cord: ' + str(y) + ' rad: '+ str(r))
        xcord.append(x)
        ycord.append(y)
        rad.append(r)
        
        # Drawing a circle
        # cv2.circle(source, (x-cord, ycord), radius, color in BGR format, thickness)       
        cv2.circle(image, (x, y), r, (255, 0, 0), 5)        
        cv2.circle(image, (x, y), 5, (255, 255, 255), 5) 
 
    # To iterate through all centers and draw lines to connect all centers of detected circles.    
    for i in range(len(xcord)-1):
      for j in range(1,len(xcord)):
          cv2.line(image, (xcord[i],ycord[i]), (xcord[j],ycord[j]), (0,0,0), 5)


# Storing the image.          
cv2.imwrite("Detected_Circle3.jpg", image) 

print("Successfully Created Image!")
cv2.waitKey(0) 



