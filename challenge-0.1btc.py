# outputs bip39 words based on table on challenge image
# based on https://www.reddit.com/r/Bitcoin/comments/9kq7it/introducing_the_310_btc_bitcoin_challenge/e7g1emc/
# tips to: 1Fnv5AjLoZiCQCypVwPFjW2pimS9TgZ5xZ

key = "20181002"
encrypted = "511B2033232841053022B0FE52ED0F7A165B52C7E75112F656FC4B"
decrypted = []
segment = ""
for i in range(len(encrypted)):
	segment = segment + format(((int(encrypted[i],16)-int(key[i%len(key)])) % 16), 'x')
	if((i+1)%3 == 0):
		decrypted.append(segment)
		segment = ""
	
print("decrypted table:" + str(decrypted))

f = open('english.txt', 'r')
words = f.readlines()
f.close()


for i in range(6,len(decrypted)):
	print(decrypted[i])
	print(words[int(decrypted[i],16)-1])