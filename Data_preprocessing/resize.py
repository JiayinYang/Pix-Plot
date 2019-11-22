import os, sys
from PIL import Image

path = '/Users/jenny/Desktop/pix-plot-masterv2/output/thumbs/128px'
path2 = '/Users/jenny/Desktop/pix-plot-masterv2/output/thumbs/128px_Resize'

for filename in os.listdir(path):
    print(filename)
    #im = Image.open(filename) 
    fileType = os.path.splitext(file)
    if fileType[1] == '.png':
     #   out = im.resize((128,128),Image.ANTIALIAS)
      #  out.save()