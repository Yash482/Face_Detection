# Face_Detection
It clearly detects the face and eye using web cam
Detection is done by applying Viola-Jones algorithm using onenCV

We first detect the face and then we detect eyes in the region of face only not on entire image.
This is done to decrease the computational time.

Our detection function takes in an image and its gray scale form also. 
After detecting, it returns the processed image. It means we are doing detection frame by frame.

# Smile Detection
Similar to the eyes, we detect the smile within the face only not on entire image.
By changing the value of neighbour factors, we got a very good result
