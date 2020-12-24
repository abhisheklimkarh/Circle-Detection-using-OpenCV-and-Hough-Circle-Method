# Circle-Detection-using-OpenCV


Detect circles in the image and draw straight lines connecting centres of circles using OpenCV.


Libraries required:

1. OpenCV :- pip install opencv-python
2. Numpy  :- pip install numpy

Algorithm:

1. Import libraries.

2. Read the image.

3. Convert the image into grayscale.

4. Use Gaussian Blur to blur the image.

	Specify the height and width of the kernel which should be positive and odd according to the image.
	
5. Use Hough Gradient method to detect circles in the image
This meth

detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1.3, 250, param1= None, param2 = None, minRadius=0, maxRadius=0)

  gray_blurred: Grayscale image input

  cv2.HOUGH_GRADIENT: Method to detect circles

  dp:	 Inverse ratio of the accumulator resolution of the image. Bigger the matrix, smaller is the value of dp, 
  higher the resolution, more accurate the circle detection. However, one has to specify this parameter according to
  their image size, otherwise it may detect multiple circles 	or miss slightely degenerated circle.

  minDist: Minimum distance between the center (x,y) coordinates of the detected circle.
  Again, this value varies from image to image. It is a crucial parameter depending the size of the actual image.
  Smaller the image size, smaller will be the value and vice versa. So, specify the size accordingly. 

  param1:  First method-specific parameter. In case of HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).

  param2:  Second method-specific parameter. In case of  HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it 		    is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.

  minRadius:	Minimum circle radius.

  maxRadius:	Maximum circle radius.

6. Creating 'xcord', 'ycord', and 'rad' lists to store the X, Y, co-ordinates and radius of detected circles.

7. Append the co-ordinates to their respective list.

8. Drawing a circle

  cv2.circle(source, (x-cord, ycord), radius, color in BGR format, thickness) 

9. Iterate through list 'xcord' and 'ycord' to retrieve center co-ordinates and draw line joining the two centers of detected circles.

10. Write the image 

 
