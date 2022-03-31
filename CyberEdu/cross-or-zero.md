# Initial Problem Statement
```
Can you find the key and the flag? I bet. It is not an encryption. It is ZERO. 
```

## We are given the following python script:
```py
import itertools
import base64

def string_xor(s, key):
    key = key * int((len(s) / len(key) + 1))
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(s, key)).encode()

flag = ""
key  = ""

print(base64.b64encode(string_xor(flag, key)))

# dHNkdktTAVUHAABUA1VWVgIHBAlSBAFTBAMFUwECAgcAAAFWAFUFCFMACFFUAwQAVgBSBwQJBVZTAFYGCQYHVQABB1IJTQ==
```



```py
flag = "dHNkdktTAVUHAABUA1VWVgIHBAlSBAFTBAMFUwECAgcAAAFWAFUFCFMACFFUAwQAVgBSBwQJBVZTAFYGCQYHVQABB1IJTQ=="
trueflag = ""
key = 0x30

flag = base64.b64decode(flag).hex()

for i in range(0, len(flag), 2):
    x = int(flag[i:i+2],16)
    trueflag = trueflag + chr(x ^ int(key))

print(trueflag)
```