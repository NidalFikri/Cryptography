def brute_force () :
    msg = bytearray(b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""")
    key = bytearray(b"ICE")
    for i in range(len(msg)) :
        msg[i]=msg[i]^key[i%3]
    return msg.hex()

print(brute_force())
