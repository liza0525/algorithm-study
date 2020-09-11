# 2019 KAKAO BLIND RECRUITMENT
import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self,nodeinfo):
        self.value = sorted(nodeinfo, key=lambda x: -x[1])[0]
        left_list = list(filter(lambda x: x[0] < self.value[0], nodeinfo))
        right_list = list(filter(lambda x: x[0] > self.value[0], nodeinfo))

        self.left_tree = Tree(left_list) if left_list else None
        self.right_tree = Tree(right_list) if right_list else None

def solution(nodeinfo):
    full_tree = Tree(nodeinfo)
    prefix_res, postfix_res = [], []

    def prefix(tree):
        prefix_res.append(nodeinfo.index(tree.value)+1)
        if tree.left_tree:
            prefix(tree.left_tree)
        if tree.right_tree:
            prefix(tree.right_tree)

    def postfix(tree):
        if tree.left_tree:
            postfix(tree.left_tree)
        if tree.right_tree:
            postfix(tree.right_tree)
        postfix_res.append(nodeinfo.index(tree.value)+1)

    prefix(full_tree)
    postfix(full_tree)

    return [prefix_res, postfix_res]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# reference
# https://programmers.co.kr/questions/3723
# https://kyome.tistory.com/111