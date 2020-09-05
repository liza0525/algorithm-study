# 2020 KAKAO BLIND RECRUITMENT
from collections import defaultdict
class Node():
    def __init__(self, char, data=None, length=None):
        self.char = char # 단 하나의 글자
        self.data = data # 마지막 글자를 나타내는 flag 보통은 boolean형
        self.children = {} # dictionary(key : char, value: 해당 char를 가진 Node)
        self.length = defaultdict(int) # length를 저장할 dictionary
 
class Trie():
    def __init__(self):
        self.head = Node(None)

    # insert(트라이에 문자열 삽입)
    def insert(self, string):
        curr_node = self.head

        curr_node.length[len(string)] += 1
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            curr_node.length[len(string)] += 1


        curr_node.data = string

    def starts_with(self, prefix, l):
        curr_node = self.head
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
        return curr_node.length[l]


def solution(words, queries):
    answer = []
    trie_front = Trie()
    trie_back = Trie()

    for word in words:
        trie_front.insert(word)
        trie_back.insert(word[::-1])

    for query in queries:

        if query == "?" * len(query):
            answer.append(trie_front.head.length[len(query)])
        elif query[0] == "?":
            prefix = query[::-1].split('?')[0]
            answer.append(trie_back.starts_with(prefix, len(query)))
        else:
            prefix = query.split('?')[0]
            answer.append(trie_front.starts_with(prefix, len(query)))


    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# reference
# https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EC%B9%B4%EC%98%A4-2020-recruit-%EA%B0%80%EC%82%AC-%EA%B2%80%EC%83%89-Level-4
# https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-trie_front-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0