#!/usr/bin/env python
"""
Encode and Decode
"""
import re
import string
import itertools as it

def encode(obj):
    """
    Encode a list
    >>> encode([b'a', 42, [13, 14]]) == b'l1:ai42eli13ei14eee'
    True
    """
    if isinstance(obj, int):
        return b"i" + str(obj).encode() + b"e"
    elif isinstance(obj, bytes):
        return str(len(obj)).encode() + b":" + obj
    elif isinstance(obj,list):
        return b"l"+b"".join(map(encode,obj))+b"e"
    else:
        raise ValueError('should be bytes')
    raise ValueError("Allowed types: int, bytes, list, dict; not %s", type(obj))

def decode(s):
    """
    Decode a List
    >>> decode(b'l1:ai42eli13ei14eee') == [b'a', 42, [13, 14]]
    True
    """   
    def decode_first(s):
        if s.startswith(b"i"):
            match= re.match(b"i(-?\\d+)e",s)
            return int(match.group(1)), s[match.span()[1]:]     
        elif any([s.startswith(str(i).encode())  for i in string.digits]):
            match=re.match(b"(\\d+):",s)
            ind_fin=int(match.group(1))
            ind_ini=int(match.span()[1])
            return s[ind_ini:ind_ini+ind_fin],s[ind_ini+ind_fin:]        
        elif s.startswith(b"l"):
            l = []
            rest = s[1:]
            while not rest.startswith(b'e'):
                ele,rest=decode_first(rest)
                l.append(ele)
            rest=rest[1:]
            return l,rest
        else:
            raise ValueError("Malformed input.") 
    ret,rest= decode_first(s)
    if rest:
        raise ValueError("Malformed input")
    return ret
                   

        




if __name__ == "__main__":
   import doctest
   doctest.testmod()    
