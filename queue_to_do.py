# def solution(start, length):
#     return _solution(start, length, None, 0)

# def _solution(start, length, checksum, to_skip):
#     if to_skip == length:
#         return checksum
#     for i in range(start, start + length - to_skip):
#         if checksum is None:
#             checksum = start
#         else:
#             checksum ^= i
#     return _solution(start + length, length, checksum, to_skip + 1)

# def solution(start, length):
#     checksum = 0
#     for j in range(0, length):
#         for i in range(start, start + length - j):
#             checksum ^= i
#         start += length
#     return checksum

def solution(start, length):
    def helper(value):
        results = [value, 1 , value + 1, 0]
        return results[value % 4]
    checksum = 0
    for j in range(0, length):
        checksum ^= helper(start - 1) ^ helper(start + length - j - 1)
        start += length
    return checksum
    

print(solution(0, 3))
print(solution(17, 4))
print(solution(22, 5))
print(solution(0, 2))