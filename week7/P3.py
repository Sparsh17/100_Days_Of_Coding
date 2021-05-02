from itertools import permutations


def to_int(nums):
    return int(''.join(map(str, nums)))


def is_interesting(num):
    n = 0
    for d in [2, 3, 5, 7, 11, 13, 17]:
        n = n + 1
        nums = [num[n], num[n + 1], num[n + 2]]
        if not to_int(nums) % d == 0:
            return False

    return True


print (sum([to_int(n) for n in permutations(range(10)) if is_interesting(n)]))