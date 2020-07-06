# 나중에 해시로 다시 풀 것
def solution(phone_book):
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            ilen = len(phone_book[i])
            jlen = len(phone_book[j])
            if phone_book[i] in phone_book[j][:ilen] or phone_book[j] in phone_book[i][:jlen]:
                return False
    return True