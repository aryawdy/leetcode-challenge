# Time : O(nlogn)
# Space : O(1)

def validAnagram(s,t):
    if len(s) != len(t):
        return False
    
    sortS = sorted(s)
    sortT = sorted(t)

    for i in range(len(sortS)):
        if sortS[i] != sortT[i]:
            return False
    
    return True

validAnagram("anagram","nagaram")