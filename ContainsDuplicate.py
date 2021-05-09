def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    found = {}
    for num in nums:
        if num in found:
            return True
        else:
            found[num] = True

    return False
