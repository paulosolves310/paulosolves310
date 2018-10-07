# extracts gzip file which contains base64 string, which decodes to openssl salted data
# donations to: 1Fnv5AjLoZiCQCypVwPFjW2pimS9TgZ5xZ

from PIL import Image
import sys

im = Image.open('challenge.png')
pix = im.load()

count = 0
rChannelByte = 0
aChannelByte = 0
rChannelBytes = []
aChannelBytes = []
for x in range(2944):
	rChannelByte = rChannelByte | (pix[x,310][0]%2 << 7-count)
	aChannelByte = aChannelByte | ((pix[x,310][3]%2 + 1) % 2 << 7-count)
	count += 1
	if(count == 8):
		aChannelBytes.append(aChannelByte)
		rChannelBytes.append(rChannelByte)
		rChannelByte = 0
		aChannelByte = 0
		count = 0

gzipBytes = bytes([rChannelBytes[x] ^ aChannelBytes[x] for x in range(len(rChannelBytes))])

with open("file.gzip","wb") as f:
	f.write(gzipBytes)