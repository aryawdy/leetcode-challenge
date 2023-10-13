

def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not isAlpaNum(s[left]):
            left += 1

        while right < left and not isAlpaNum(s[right]):
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1
    
    return True


def isAlpaNum(char):
    return (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))


isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("race a car")