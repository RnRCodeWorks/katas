def atbash_cypher(msg):
    decoded = []
    for c in list(msg):
        val = ord(c)
        if 91 > val > 64:
            decoded.append(chr(155-val))
        elif 123 > val > 96:
            decoded.append(chr(219-val))
        else:
            decoded.append(chr(32))
    return str.join( '', decoded)
