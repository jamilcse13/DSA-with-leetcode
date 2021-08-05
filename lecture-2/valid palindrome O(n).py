class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ""
        for i in s:
            if i.isalnum() == True:
                f += i.lower()
        left = 0
        right = len(f)-1
        
        while left<right:
            if f[left] != f[right]:
                return False
            left += 1
            right -= 1
        return True
      
      
# Input: isPalindrome("A man, a plan, a canal: Panama")
# Output: true

# Input: isPalindrome("race a car")
# Output: false
