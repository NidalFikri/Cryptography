
def brute_force(msg,key) :
    msg = bytearray.fromhex(msg)
    for i in range(len(msg)) :
    	msg[i] = msg[i]^key
    return msg

#English = "abcdefghijklmnopqrstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'0123456789"
f = open("enc","r")
str =f.readlines()
cnt = 1
for line in str :
    print("Line number {}  ### ".format(cnt))
    cnt+=1
    for i in range(256) :
         dec = brute_force(line,i)
         if b" " and b'the' in dec :	# :"D no freq. analysis , no bullshit :"D
            print(dec)

