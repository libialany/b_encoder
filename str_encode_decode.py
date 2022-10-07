#!/usr/bin/env python
import re
import string

def encode(obj):
    """


    >>> encode('Pyladies')
    b'8:Pyladies'
    """    
    if isinstance(obj, str):
    #    return encode(obj.encode('ascci'))+ b':'+ obj.encode()
        return str(len(obj)).encode()+ b':'+ obj.encode()
    #if isinstance(obj, bytes):
    #   return str(len(obj)).encode()


def decode(s):
    """
    >>> decode(b'8:Pyladies') 
    b'Pyladies'
    """ 
    def decode_first(s):
        if any([s.startswith(str(i).encode())  for i in string.digits]):
            match=re.match(b"(\\d+):",s)
            ind_fin=int(match.group(1))
            ind_ini=int(match.span()[1])
            return s[ind_ini:ind_ini+ind_fin],s[ind_fin:]
    return decode_first(s)[0]
            
if __name__=="__main__":
    import doctest
    doctest.testmod()