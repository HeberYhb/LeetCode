def lengthOfLongestSubstring(s):
    if (s == ""):
        return 0
    maxlen = 1
    lens = 0
    subS = ''
    i = 0
    while (i < len(s)):
        if s[i] not in subS:
            subS += s[i]
        else:
            tmp = subS.find(s[i])
            start = i - len(subS) + tmp + 1
            end = i + 1
            subS = s[start:end]
        lens = len(subS)
        if (lens > maxlen):
            maxlen = lens
        i = i + 1
    return maxlen

s=input()
lengthOfLongestSubstring(s)