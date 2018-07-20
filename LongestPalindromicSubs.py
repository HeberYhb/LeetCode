#暴力法
def longestPalindrome(s):
    x=len(s)
    if(x==0):
        return ""
    while(x>0):
        for i in range(len(s)-x+1):
            subString=s[i:i+x]
            end=len(subString)-1
            start=0
            flag=1
            while(start<=end):
                if(subString[start]!=subString[end]):
                    flag=0
                    break
                else:
                    start=start+1
                    end=end-1
            if(flag==1):
                result=subString
                break
        x = x - 1
        if(flag==1):
            break
    return result
s=""
result=longestPalindrome(s)
print(result)