# Importing Image class from PIL module
from PIL import Image
import random as rand
 
# Opens a image in RGB mode
fileName = input("Enter image name(Must be withing same folder/directroy): ")
im = Image.open(fileName)
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# showing the initial height and width
print("Height: " , height , ", Width: " , width)

# this part is only for cropping image
# Setting the points for cropped image
left = 0
top = 0
right = width
bottom = height
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))



# take user input
user_width = int(input("Enter your width: "))
user_height = int(input("Enter your height: "))

# resize the image
newsize = (user_width, user_height)
im1 = im1.resize(newsize)

# Shows the image in image viewer and save it
im1.show()
sl = str(rand.randrange(1000,9999)) # random serial number
im1.save("Resized_Wallpaper_" + sl + ".jpg")