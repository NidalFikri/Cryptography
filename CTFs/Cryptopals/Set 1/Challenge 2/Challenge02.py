

def xor_hex (str_1,str_2) :
    str_1 = bytearray.fromhex(str_1)
    str_2 = bytearray.fromhex(str_2)
    for i in range(len(str_1)) :
        str_1[i] = str_1[i]^str_2[i]
    return str_1.hex()



print(xor_hex("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))
    
