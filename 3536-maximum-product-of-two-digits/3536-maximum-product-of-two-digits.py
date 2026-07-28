class Solution:
    def maxProduct(self, n: int) -> int:
        r=n
        a=[]
        i=0
        while r!=0:
            digit=r%10
            a.append(digit)
            i=i+1
            r=r//10
        ans=a[0]*a[1]
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if (a[i]*a[j] )> ans:
                    ans=a[i]*a[j]
        
        return ans