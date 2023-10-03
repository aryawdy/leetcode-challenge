from collections import defaultdict
# Time : O(mnlogn)
# Space : O(mn)
def groupAnagram(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    print(anagram_map.values())
    return list(anagram_map.values())




groupAnagram(["eat","tea","tan","ate","nat","bat"])