class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero=0
        one=0
        two=0

        for i in range(len(nums)):
            if nums[i]==0:
                zero=zero+1
            elif nums[i]==1:
                one=one+1
            elif nums[i]==2:
                two=two+1
        ans=[]
        for i in range(0,zero):
            ans.append(0)
        for i in range(0,one):
            ans.append(1)
        for i in range(0,two):
            ans.append(2)
        
        for i in range(len(nums)):
            nums[i]=ans[i]
        