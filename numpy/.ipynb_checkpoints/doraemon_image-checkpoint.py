import numpy as np
import matplotlib as mp
import matplotlib.image as mpimg

img = mpimg.imread("numpy\Doraemon-1.jpg")
print(type(img))
print(img.shape)
# with open("temp.txt","w") as file :
#     file.write(np.array2string(img,threshold=np.inf,separator=","))
cop = img.copy()
cop[:,:,:2] = 0 
mpimg.imsave("numpy/blue.jpg",cop)