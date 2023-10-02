def sortWord(word):
    return ''.join(sorted(word))


def groupAnagram(strs):
    sortedStrs = list(map(sortWord,strs))
    print(sortedStrs)
    resultIndex = list()
    i = 0
    while i < len(sortedStrs):
        j=0
        while j < len(sortedStrs):
            # print(sortedStrs[i], i, j, len(sortedStrs))
            if sortedStrs[i] == sortedStrs[j]:
                resultIndex.append(j)
            j +=1
        i +=1
        

    print(resultIndex)



    return True

groupAnagram(["eat","tea","tan","ate","nat","bat"])