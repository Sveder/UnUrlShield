import os
import sys
import copy

from PIL import Image
from pygame.colordict import THECOLORS as COLORS

#Minimum number of pixels per letter:
MIN_PIXEL_PER_LETTER_COUNT = 250

#Store locations for each color type:
class PixelLoc():
    def __init__(self, color_tup):
        self.color_tup = color_tup
        self.loc = []
        self.count = 1
        
#Open the input file and the out file:
inp = Image.open(sys.argv[1], "r")
out = Image.new("RGBA", inp.size, (255, 255, 255))
print "Input image side: %s" % (str(inp.size), )
#String for resetting the image back to black:
reset_str = out.tostring()

color_dict = {}
for i in xrange(inp.size[0]):
    for j in xrange(inp.size[1]):
        cur_pixel = inp.getpixel((i, j))
        
        #Save all the color locations for each color:
        if color_dict.has_key(cur_pixel):
            color_dict[cur_pixel].count += 1
        else:
            color_dict[cur_pixel] = PixelLoc(cur_pixel)
        
        color_dict[cur_pixel].loc.append((i, j))
        
        #if (0, 0, 0) == cur_pixel:
        #    out.putpixel((i, j), (255, 255, 255))
        #else:
        #    out.putpixel((i, j), cur_pixel)
            
#Find only colors over the min count:
big_dict = {}
for i in color_dict.keys():
    if color_dict[i].count > MIN_PIXEL_PER_LETTER_COUNT:
        big_dict[i] = color_dict[i]
        
#Create a picture for each letter (by the count):
counter = 0
for color in big_dict.keys():
    print "Key >>>", color
#    print "color: %s, locations: %s" % (str(big_dict[color].color_tup), big_dict[color].loc)
    #Make it black for easier recognition:
    for i in big_dict[color].loc:
        out.putpixel(i, (0, 0, 0))
    
    #Save the picture and reset the image object:
    out.save("parsed%s.png" % (counter))
    counter += 1
    out.fromstring(reset_str)

print "ended!"