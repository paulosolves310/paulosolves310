# base64 string from line 310 alpha channel which decodes to openssl salted data
# donations to: 1Fnv5AjLoZiCQCypVwPFjW2pimS9TgZ5xZ

from PIL import Image
import sys
import base64

challengeImg = Image.open('challenge.png')
pixels = challengeImg.load()

count = 0
aChannelByte = 0
aChannelBytes = []
for x in range(2944):
	aChannelByte = aChannelByte | ((pixels[x,310][3]%2) << 7-count)
	count += 1
	if(count == 8):
		aChannelBytes.append(aChannelByte)
		aChannelByte = 0
		count = 0

with open("challenge.enc","wb") as f:
	f.write(base64.b64decode(bytes(aChannelBytes)))