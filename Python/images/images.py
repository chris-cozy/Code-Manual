from PIL import Image

# Opening an image
# Image.open(filepath)
# Produces a specialized jpeg image file from PIL
mac = Image.open('images\example.jpg')

# Built-in Attributes
    # size - returns (width, height)
    # filename - returns filename
    # format_description - returns the international standard of jpeg that the file is
print(mac.size)
print(mac.filename)
print(mac.format_description)

# Built-in Functions
    # show() - Display the image
        # Opens a window, displaying the image
    # crop() - Input a tuple of two sets of coords, 
    # one for the starting point, and one for the width and height of the crop (x,y,w,h)
        # Returns the cropped image
    # paste() - Paste an image over an image (im= image to paste, box = (starting point))
        # A mask can be added, with the same value as the im
        # Permanently affects the variable, but not the image itself.
    # resize() - tuple of (new width, new height)
        # Resizes and returns image
    # rotate() - degrees to rotate (90)
        # Rotates and returns image
mac.show()
mac_2 = mac.crop((50,50,1000,1000))
mac_2.show()
mac.paste(im=mac_2, box = (0,0))
mac.show()

# Color transparency (RGBA - Red, Green, Blue, Alpha)
# Alpha controls transparency
    # Alpha = 0, image is completely transparent
    # Aplha = 255, image is completely opaque
# putalpha() - Change the alpha value 0 - 255
red = Image.open("images\\red_color.jpg")
blue = Image.open('images\\blue_color.png')
red.putalpha(128)
blue.putalpha(128)

blue.paste(im = red, box = (0,0), mask = red)
blue.show()

# Saving new image
# save(filepath/filename)
blue.save("images\\new.jpg")