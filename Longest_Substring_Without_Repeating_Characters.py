class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        """Bruteforce method
        def check(start,end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
        
        n = len(s)
        
        res = 0
        for i in range(n):
            for j in range(i,n):
                if check(i, j):
                    res = max(res, j-i+1)
        return res            
        Time limit exceeded O(n^3)"""
        
        """Sliding window approach
        chars = [0] * 128
        left = right = 0
        res = 0
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
                
            res = max(res, right - left + 1)      
         
            right += 1
            
        return res     
        """
        chars = [None] * 128
        
        left = right = 0
        res = 0
        
        while right < len(s):
            r = s[right]
            
            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1
                
            res = max(res, right - left + 1)
            
            chars[ord(r)] = right
            right += 1
            
        return res    
        
 
myobj =  Solution()    
res= myobj.lengthOfLongestSubstring("abcabcbb")
print(res)
                
                
                
                
                
                
        