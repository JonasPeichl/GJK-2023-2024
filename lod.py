
def win1(t, s, v = 0):
    while t*v <= s:
        t = t-1
        v = v+1
    return t-v+1

a = win1(71530, 940200)
b = win1(41667266, 244104712281040)
c = win1(72, 1228)
d = win1(66, 1040)

print(b)