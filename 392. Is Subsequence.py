class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag= False
        j=0
        if s== "":
            flag= True
            return flag
        elif j== "":
            flag= False 
            return flag
        for i in range(len(t)):
            if s[j]== t[i]:
                flag = True
                if j + 1 >= len(s):
                    return flag
                else:
                    j+= 1
            else:
                flag= False
                continue
        if j != len(s):
            flag= False
        return flag            

mysol= Solution()
print(mysol.isSubsequence("abh", "ahbgdc"))