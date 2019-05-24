import os

import math
from PIL import Image

iphone5_w = 1366
iphone5_h = 640

dir = 'resource/'
images = os.listdir(dir) # 列出文件夹下所有的目录与文件

for image in images:
    im = Image.open(dir + str(image))
    w, h = im.size
    print(w, h)
    if w > iphone5_w:
        scale = iphone5_w / float(w)
        new_h = math.ceil((float(h)*float(scale)))
        im = im.resize((iphone5_w, new_h), Image.ANTIALIAS)
    if h > iphone5_h:
        scale = iphone5_h / float(h)
        new_w = math.ceil((float(w) * float(scale)))
        im = im.resize((new_w, iphone5_h), Image.ANTIALIAS)
    im.save(dir + 'new_' + str(image), 'png')
