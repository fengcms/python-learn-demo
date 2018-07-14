#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from PIL import Image
im = Image.open("test.jpg")
mark=Image.open("mark.png")
layer=Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-170,im.size[1]-60))
out=Image.composite(layer,im,layer)
out.show()
out.save('target.jpg', 'JPEG', quality = 100)
