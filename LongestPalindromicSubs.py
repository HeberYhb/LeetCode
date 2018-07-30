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


#动态规划法
def DPLogestPalindrome(s):
    lens=len(s)
    if(lens<2):
        return s
    maxlen=1    #最长回文子串的长度
    start=0     #回文的开始位置
    # 定义一个nxn维的数组,初始化全为0，用来标记哪些子串是回文，例如dp[i][j]=1表示s[i:j]是一个回文
    dp=[[0]*lens for i in range(lens)]

    #第一步：将单个字符标为回文，并且找出长度为2的回文
    for i in range(lens):
        dp[i][i]=1
        #print(dp)
        if i<lens-1 and s[i]==s[i+1]:
            dp[i][i+1]=1
            start=i
            maxlen=2

    #第二步：从长度3开始逐步找出回文子串
    for i in range(3,lens+1):        #i代表查找回文子串的长度
        for j in range(0,lens-i+1):  #j表示子串的起始位置
            end=j+i-1                #子串结束位置
            if dp[j+1][end-1] and s[j]==s[end]:  #若aba是回文，那么*aba#中若*=#则*aba#也是回文
                dp[j][end]=1
                start=j
                maxlen=i

    #返回最长回文子串
    return s[start:start+maxlen]

s="aaaaaaa"
#result=longestPalindrome(s)
result=DPLogestPalindrome(s)
print(result)