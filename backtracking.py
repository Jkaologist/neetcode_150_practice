def subsetsWithDup(nums):
    nums.sort()
    out = []
    
    def backtrack(i = 0, path = []):
        if i == len(nums):
            out.append(path[:])
            return
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(i + 1, path)
    backtrack()
    return out


def subsetsWithDup2(nums):
    def backtrack(start = 0, tempList = []):
        results.append(list(tempList))
        for i in range(start, len(nums)):
            # skip duplicate
            if i > start and nums[i - 1] == nums[i]: continue
            # add each num to tempList
            tempList.append(nums[i])
            # include curr number and move fwd
            backtrack(i + 1, tempList)
            # remove the curr num
            tempList.pop()
    results = []
    # sort to ensure duplicates are adjacent
    nums.sort()
    backtrack()
    return results

