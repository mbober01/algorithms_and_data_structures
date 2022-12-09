def max_num(nums):
    nums = [float(x) for x in nums.split(";")]
    max = nums[0]
    for x in nums:
        if x > max:
            max = x
    return max

print(max_num("1;3;5;2;2.1"))
