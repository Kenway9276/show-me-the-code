from PIL import Image, ImageDraw, ImageFont

im = Image.open("0001.jpg")
draw = ImageDraw.Draw(im)
font_size = im.size[0]/4
font = ImageFont.truetype('lucon.ttf', int(font_size))
x = im.size[0] - font_size
draw.text((x, 0), '4', font=font, fill='red')
im.show()
