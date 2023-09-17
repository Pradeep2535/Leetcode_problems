'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p,z,n=[],[],[]
        
        res=set()
        for i in nums:
            if i>0:p.append(i)
            elif i==0:z.append(i)
            else:n.append(i)
        P =set(p)
        N=set(n)
        if len(z)>=3:
            res.add((0,0,0))
        if z:
            for i in P:
                if -1*i in N:
                    res.add((i,-i,0))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if -1*(p[i]+p[j]) in N:
                    res.add(tuple(sorted((p[i],p[j],-1*(p[i]+p[j])))))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                c=-1*(n[i]+n[j])
                if c in P:
                    res.add(tuple(sorted((n[i],n[j],c))))

        return res
