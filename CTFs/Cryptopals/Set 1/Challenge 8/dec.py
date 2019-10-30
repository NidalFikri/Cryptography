f = open("enc.txt",'r')

def detect_ECB (block,str1) :
    i = 0
    while i < 320 :
        chunk = str1[i:i+16]
        if chunk in str1[i+16:] :
            return True , block
        i+=16
    return False,-1

def print_block(no) :
    f.seek(0)
    str1 = f.read()[0+320*no:320+320*no]
    print(str1)

block = 1
det_list = []

while True :
    str1 = f.read(320)
    str2 = bytearray(f.read(320))
    status,no = detect_ECB(block,str2)    
    if status :
        print("Block number : {}".format(no))
        det_list.append(no-1)        
    if len(str1) < 320 :
        break
    block+=1

for x in det_list :
    print_block(x)

f.close()
