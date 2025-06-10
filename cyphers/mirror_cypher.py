# The challenge with this one is to make a cypher similar to the Atbash method, mirror method, but add in a second
#   argument that accepts a seed of "mirrored letters"
#   ie if 'abcde' was passed in with 'acnm' -> it would then return 'mbnde' instead of 'zyxwv'
#   if no secondary string is passed then a normal mirror is applied
#
# *** based on challenge returned message should only be lower case


def mirror(code, seed = None):
    code = code.lower()
    if seed is None:
        return str.join('', [x if not 123 > ord(x) > 96 else chr(219 - ord(x))  for x in list(code)])
    elif seed == '':
        return code
    else:
        seed_list = list(seed)
        return str.join('', [x if x not in seed_list else seed[len(seed)-1-seed_list.index(x)] for x in list(code)])


# alternative solution not mine but I like the execution

# from string import ascii_lowercase as lowercase
# def mirror(code, chars=lowercase):
#     return code.lower().translate(str.maketrans(chars, chars[::-1]))