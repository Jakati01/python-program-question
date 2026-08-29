class solution:
    def consectuive  (self, nums, k ):
        

        window_sum =sum(nums[:k])
        maximum =window_sum

        for i in range (k,len(nums)):
            window_sum = window_sum - nums[i-k] +nums [i]
            maximum = max(maximum,window_sum)

        return maximum

obj = solution()

result = obj.consectuive([2,1,5,1,3,2] , 3)

print(result)

