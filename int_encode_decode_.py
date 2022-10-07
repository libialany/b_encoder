#!/usr/bin/env python
import re
import string

def encode(obj):
    """
    encode

    >>> encode(-2)
    b'i-2e'
    """    
    if isinstance(obj, int):
        return b"i" + str(obj).encode() + b"e"

def decode(s):
    """
    decode

    >>> decode(b'i-2e') 
    -2
    """ 
    def decode_first(s):
        if s.startswith(b"i"):
            match= re.match(b"i(-?\\d+)e",s)
            return int(match.group(1)), s[match.span()[1]:]
    return decode_first(s)[0]
            
if __name__=="__main__":
    import doctest
    doctest.testmod()
