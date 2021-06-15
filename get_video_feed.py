# import the opencv library
import cv2
import numpy as np


def resize_to_half_inefficient(image):

    resized_image = []

    scale_factor = 2
    
    k = 0
    for i in range(0, image.shape[0], scale_factor):
        row = []
        for j in range(0, image.shape[1], scale_factor):
            row.append(image[i][j])
        resized_image.append(row)
            
            
    return resized_image

def resize_to_half(image):

    scale_factor = 2

    resized_image = np.zeros( (int(image.shape[0]/scale_factor), int(image.shape[1]/scale_factor)) )

    
    k = 0
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            resized_image[i] = (image[i][j])
        resized_image.append(row)
            
            
    return resized_image


def _thresholding(img, threshold):

    thresholded_img = []
    

        
    dim = len(img.shape)
    print (dim)

    if dim == 2:
        for row in img:
            thresholded_img_row = []    
            for pixel in row:           
    #             print ("pixel is" , pixel)
                thresholded_img_row.append ((1 if pixel > threshold else 0))
            thresholded_img.append(thresholded_img_row)



    elif dim == 3:
        for row in img:
            thresholded_img_row = []    
            for pixel in row:           
#                 print ("pixel is" , pixel)
                thresholded_img_row.append ((1 if pixel[0] > threshold else 0))
            thresholded_img.append(thresholded_img_row)


    
    return thresholded_img



  
# define a video capture object
vid = cv2.VideoCapture(0)
  
# Capture the video frame
# by frame
ret, frame = vid.read()

scale_percent = 10 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # resized_image = np.array(resize_to_half_inefficient(frame))
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    # cv2.resize()

    # Display the resulting frame
    cv2.imshow('frame', resized)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()