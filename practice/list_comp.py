

def squares(nums: list[int])->list[int]:
    return [x**2 for x in nums]
def keepevens(nums: list[int])->list[int]:
    return [x for x in nums if x % 2 == 0]
def keepodd(nums: list[int])->list[int]:
    return [x for x in nums if x % 2 != 0]
def keepints(nums: list)->list[int]:
    return [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]