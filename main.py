import random
import time
from typing import List


def CreateHash():
        ws: List[int] = []
        for i in range(26):
            ws.append(0)
        return ws

def ClearHash(ws):
    for i in range(26):
        ws[i] = 0
    return ws

def HashCheck(str1, str2, wsHash):

    ws = ClearHash(wsHash)
    HashStrings(str1, str2, ws)
    ret = CheckHashTableEmpty(ws)
    return ret

def HashStrings(str1, str2, ws):
    for w in str1:
        i = ord(w) - ord('A')
        ws[i] = ws[i] + 1

    for w in str2:
        i = ord(w) - ord('A')
        ws[i] = ws[i] - 1

def CheckHashTableEmpty(ws):
    ret = True
    for d in ws:
        if d != 0:
            ret = False
            break
    return ret

def SortCheck(str1, str2):
    s_str1 = sorted(str1)
    s_str2 = sorted(str2)
    if s_str1 == s_str2:
        return True
    else:
        return False

def RandomWordGen(wLen):
    wrd = []
    for w in range(wLen):
        ch = chr(random.randint(ord('A'), ord('Z')))
        wrd.append(ch)
    return wrd


def RunSortHashCheck(rng, wlStart, wlEnd):
    wsHash = CreateHash ()
    for j in range(rng):
        wordLen = random.randint ( wlStart, wlEnd )
        str1 = RandomWordGen(wordLen)
        str2 = RandomWordGen(wordLen)
        c = SortCheck(str1, str2)
        c = HashCheck ( str1, str2, wsHash )


if __name__ == '__main__':
    rng = 100000
    wlStart = 2
    wlEnd = 100

    RunSortHashCheck(rng, wlStart, wlEnd)






