import base64
from Crypto.Cipher import AES

f = open("enc",'r')     #original cipher text
f2 = open("decrepted",'a')  #final secret plain text
f3 = open("b64_decoded",'w')    #base64 decoded cipher text 

obj = AES.new("YELLOW SUBMARINE",AES.MODE_ECB)
b64_decoded = base64.b64decode(f.read())
f3.write(b64_decoded)

f3.close()
f3 = open("b64_decoded",'r')

while True :
    cipher = f3.read(16)
    f2.write(obj.decrypt(cipher))
    if len(cipher) < 16 :
        break

f.close()
f2.close()
f3.close()
