class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result= ""
        minlen=0

        if len(word1) > len(word2):
            minlen += len(word2)
        else:
            minlen += len(word1)
        
        for i in range(minlen):
            result += word1[i:i+1:1] + word2[i:i+1:1]
        
        if len(word1) > len(word2): 
            result +=  word1[(minlen):]
        else:
            result +=  word2[(minlen):]
        
        return result
    
word1= "abcd"
word2= "pq"

my_solution = Solution()
print(my_solution.mergeAlternately(word1, word2))
