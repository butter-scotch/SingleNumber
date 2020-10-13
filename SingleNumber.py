class Solution:
  def singleNumber(self, nums):

    pair= []

    for i in nums:
      if not i in pair:
        pair.append(i)
      else:
        pair.remove(i)
    return pair[0]

result = Solution()
print(result.singleNumber([2,2,1]))