# def solution(l):
#     count = 0
#     perms = permutations(l, [], [], 3)
#     for per in perms:
#         res = 0
#         res |= per[1] % per[0]
#         res |= per[2] % per[1]
#         if res == 0:
#             count += 1
#     return count


# def permutations(values, per, perms, length):
#     if len(per) == length:
#         perms.append(per)
#         return perms
#     if not len(values):
#         return perms
#     for idx, value in enumerate(values):
#         newPer = per.copy()
#         newPer.append(value)
#         permutations(values[idx + 1:], newPer, perms, length)
#     return perms


# def solution(l):
#     return _solution(l, 0, [], 3, 0)


# def _solution(values, startingIdx, per, perLength, count):
#     if len(per) == perLength:
#         res = 0
#         res |= per[1] % per[0]
#         res |= per[2] % per[1]
#         if res == 0:
#             count += 1
#         return count
#     if not len(values):
#         return count
#     for idx in range(startingIdx, len(values)):
#         newPer = per[:]
#         newPer.append(values[idx])
#         count = _solution(values, idx + 1, newPer, perLength, count)
#     return count


# def solution(l):
#     return _solution(l, 0, 0, 3, 0)


# def _solution(values, startingIdx, curLength, perLength, result):
#     if curLength == perLength:
#         return result + 1
#     for idx in range(startingIdx, len(values)):
#         if not startingIdx or not values[idx] % values[startingIdx - 1]:
#             result = _solution(values, idx + 1, curLength + 1, perLength, result)
#     return result



# def solution(l):
#     count = 0
#     for idx0 in range(len(l) - 2):
#         for idx1 in range(idx0 + 1, len(l) - 1):
#             if l[idx1] % l[idx0]:
#                 continue
#             for idx2 in range(idx1 + 1, len(l)):
#                 if not l[idx2] % l[idx1]:
#                     count += 1
#     return count


def solution(l):
    count = 0
    res = dict()
    for idx0 in range(len(l) - 1):
        for idx1 in range(idx0 + 1, len(l)):
            if not l[idx1] % l[idx0]:
                res[idx1] = res.get(idx1, [])
                res[idx1].append(idx0)
    for key, value in res.items():
        for el in value:
            count += len(res.get(el, []))
    return count


print(solution([1, 3, 4]))  # 0
print(solution([1, 2, 4]))  # 1
print(solution([1, 1, 1]))  # 1
print(solution([1, 2, 3, 4, 5, 6]))  # 3
print(solution([1, 2, 2, 4, 5, 6]))  # 7
print(solution([1, 2, 2, 4, 5, 6, 7, 8, 9, 1, 5]))  # 15