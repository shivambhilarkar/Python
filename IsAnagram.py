def areCountsEqual(c1, c2):
    for k in c1:
        if k not in c2 or c1[k] != c2[k]:
            return False
    return True

def getCharCounts(s):
    counts = dict()
    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def isAnagaram(A, B):
    if len(A)< len(B):
        return False
    countB = getCharCounts(B)
    for i in range(0, len(A)-len(B)+1):
        window = A[i: i+len(B)]
        countWindow = getCharCounts(window)

        if areCountsEqual(countB, countWindow):
            return True 
    return False


if __name__ == "_main_":
    word = input().strip()
    first_char= []
    idx = 0  #index of the first char of the string

    q = int(input())
    for _ in range(q):
        direc , s = input().strip().split()
        s= int(s)

        if direc == "L":
            idx = (idx + s) % len(word)
        else:
            idx = (idx - s) % len(word)
        first_char.append(word[idx])

    if isAnagaram(word, first_char):
        print("YES")
    else:
        print("NO")

