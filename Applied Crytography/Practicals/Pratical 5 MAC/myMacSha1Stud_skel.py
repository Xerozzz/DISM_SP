#!/usr/bin/env python3
#ST2504 - ACG Practical - myMacSha1Stud.py
from Cryptodome.Random import get_random_bytes
import hmac
import base64
import sys
# main program starts here
'''
argc = len(sys.argv)
if argc != 2:
    print("Usage : {0} <file name>".format(sys.argv[0]))
    exit(-1)
    '''
try:
    ## with open(sys.argv[1]) as f:
    with open("a.txt") as f:
        content=f.read()    # read in the entire text file
        print("A simple Program on HmacSHA1")
        keysize=hmac.HMAC.blocksize # retrieve the default block size
        print("key size {0}".format(keysize))
        # insert your code here to generate a random key
        random_key = get_random_bytes(keysize)
        # display the key in base64 encoded bytes in UTF8 format
        print("key : {0}".format(base64.b64encode(random_key).decode()))
        # insert your code here to instantiate a sha1 hmac object, hma .
        h = hmac.new(random_key,digestmod="sha1")
        # insert your code here to use hma to compute the hmac of content.
        d = h.digest()
        b64 = base64.b64encode(d)
        # insert your code here to display the HMAC digest in base64 encoded bytes in UTF8 format
        print(b64.decode())
except:
    print("Invalid file argument!")
