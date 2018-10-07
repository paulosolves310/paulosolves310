# extracts and shows QR code
# donations to: 1Fnv5AjLoZiCQCypVwPFjW2pimS9TgZ5xZ

from PIL import Image
import sys

im = Image.open('challenge.png')
pix = im.load()

count = 0
aChannelBit = []
width = 85
for x in range(1431, 1514):
	for y in range(913, 998):
		count = count + 1
		aChannelBit.append((pix[x,y][3]%2 +1) % 2)

#pad
aChannelBit.extend([0]*200)

height = int(len(aChannelBit)/width)

img = Image.new('RGB', (width,height), 'white')
pixels = img.load()

for i in range(img.size[0]):   
	for j in range(img.size[1]):
		if aChannelBit[j + width*i] == 1:
			pixels[i,j] = (255,255,255)
		else:
			pixels[i,j] = (0,0,0)

img.show()

