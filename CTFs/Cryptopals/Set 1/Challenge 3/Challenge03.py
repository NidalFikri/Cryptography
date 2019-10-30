
def brute_force(msg,key) :
	msg = bytearray.fromhex(msg)
	for i in range(len(msg)) :
		msg[i] = msg[i]^key
	return msg

str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
for i in range(256) :
	print(f"key is : {i} ----",end='')
	print(brute_force(str,i))
