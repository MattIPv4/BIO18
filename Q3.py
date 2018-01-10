serial = 146235
size = 6

def rangeCheck(r1, r2, v1, v2):
    vr = sorted([r1, r2])
    v1c = (v1 and vr[0] < v1 < vr[1])
    v2c = (v2 and vr[0] < v2 < vr[1])
    return (v1c or v2c)

def serialSwap(s, i1, i2):
    s = list(s)
    v1 = s[i1]
    v2 = s[i2]
    s[i1] = v2
    s[i2] = v1
    return int("".join(s))

def newSerial(se, i1, i2, d, m, si):
    nse = serialSwap(se, i1, i2)
    if nse not in m or m[nse]['depth'] > d:
        m[nse] = {'depth':d, 'parent':se}
        return doSearch(nse, si, d+1, m)
    else:
        return m

def doSearch(serial, size, depth=1, matches={}):
    for _ in range(size):
        serial = str(serial)
        thisDigit = int(serial[_])
        left1Digit = None if _<1 else int(serial[_-1])
        left2Digit = None if _<2 else int(serial[_-2])
        right1Digit = None if _+1>=size else int(serial[_+1])
        right2Digit = None if _+2>=size else int(serial[_+2])

        if left1Digit:
            if rangeCheck(left1Digit, thisDigit, right1Digit, left2Digit):
                matches = newSerial(serial, _, _ - 1, depth, matches, size)

        if right1Digit and False:
            if rangeCheck(right1Digit, thisDigit, right2Digit, left1Digit):
                matches = newSerial(serial, _, _ + 1, depth, matches, size)

    return matches

# 3(a)
#   Not completed
#
#   This function call will generate a dictionary of every serial generated from the source
#     The value for each key is a sub-dictionary containing the number of recursions it took to reach this combination (depth)
#     and the parent serial number to aid with debugging in the route it took to reach this combination (parent)
#
#   Stuck at trying to calculate the longest distance in the dictionary.
print(doSearch(461235,6))