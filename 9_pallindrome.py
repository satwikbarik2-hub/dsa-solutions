class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        ispallindrome=False
        num=x
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num//=10
        if rev==x:
            ispallindrome=True
        return ispallindrome