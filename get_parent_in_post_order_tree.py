# def solution(h, q):
#     result = list()
#     for node in q:
#         result.append(int(get_parent(h, node)))
#     return result


# def get_parent(h, node):  # get paraent when nodes are numerated level by level starting from right leaf
#     if node == 2**h - 1:
#         return -1
#     minVal = 2**h - 1
#     for i in range(2, h + 1):
#         maxVal = minVal - 1
#         minVal = maxVal - 2**(i - 1) + 1
#         if node <= maxVal and node >= minVal:
#             idxInRow = node - minVal
#             idxInRowParent = idxInRow // 2
#             return maxVal + 1 + idxInRowParent
#     return -1


def solution(h, q):
    result = dict()
    post_traversal(2**h - 1, -1, q, h - 1, result)
    return [result.get(node, -1) for node in q]

def post_traversal(count, parent, searched_nodes, h, result):
    if count in searched_nodes:
        result[count] = parent
    if count == 1 or h == 0:
        return count
    parent = count
    count = post_traversal(count - 1, parent, searched_nodes, h - 1, result)
    count = post_traversal(count - 1, parent, searched_nodes, h - 1, result)
    return count


print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))
print(solution(4, [15, 1, 10, 2, 3]))