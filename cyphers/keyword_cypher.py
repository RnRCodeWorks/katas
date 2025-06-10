#  Challenge was to make a cypher that took two params, 1) a message and 2) a keyword
#   Any duplicate letters in the keyword will be removed ex 'wednesday' => 'wednsay'
#   It will then be applied to the front of the alphabet, which will then be adjusted accordingly
#   Ex again with 'wednsay' applied to 'abcdefghijklmnopqrstuvwxyz', would then be 'wednsaybcfghijklmopqrtuvxz'
#   So 'a'='w', 'b'='e',...'y'='x','z'='z'

from string import ascii_lowercase as lowercase

def keyword_cypher(msg, keyword):
    shuffled_alpha=[]
    for l in list(keyword+lowercase):
        if l not in shuffled_alpha:
            shuffled_alpha.append(l)
    if len(shuffled_alpha) != 26:
        return "Invalid translation"
    return msg.lower().translate(str.maketrans(lowercase, str.join('',shuffled_alpha)))
