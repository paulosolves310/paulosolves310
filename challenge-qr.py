# extracts and saves QR code
# tips to: 1Fnv5AjLoZiCQCypVwPFjW2pimS9TgZ5xZ

from PIL import Image
import sys

challengeImg = Image.open('challenge.png')
pixels = challengeImg.load()

aChannelBit = []
for x in range(1429, 1514):
	for y in range(913, 998):
		aChannelBit.append((pixels[x,y][3]%2 +1) % 2)


width = 85
height = int(len(aChannelBit)/width)
qrImg = Image.new('RGB', (width,height), 'white')
qrPixels = qrImg.load()

for i in range(width):   
	for j in range(height):
		if aChannelBit[j + width*i] == 1:
			qrPixels[i,j] = (255,255,255)
		else:
			qrPixels[i,j] = (0,0,0)


qrImg.save('qr.png')

