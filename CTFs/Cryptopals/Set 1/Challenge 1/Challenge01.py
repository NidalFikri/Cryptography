#https://docs.python.org/3.7/library/stdtypes.html#bytes
#https://docs.python.org/3.7/library/base64.html

import base64
def hex_2_b64 (str) :
	str = bytes.fromhex(str)
	print("Raw : ",end="") ; print(str)
	return base64.b64encode(str)

str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(hex_2_b64(str))
