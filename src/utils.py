import string

CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase

def encode_base62(num):
    if num == 0:
        return CHARS[0]
    
    result = ""
    base = len(CHARS)
    
    while num:
        result = CHARS[num % base] + result
        num //= base
        
    return result
