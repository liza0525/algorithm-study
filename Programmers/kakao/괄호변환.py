# 2020 KAKAO BLIND RECRUITMENT
def solution(p):
    # 올바른지 아닌지
    def is_correct(u):
        left_b_num = 0
        for b in u:
            if b == '(':
                left_b_num += 1
            elif b == ')':
                if left_b_num:
                    left_b_num -= 1
                else:
                    return False
        return True

    # 올바른 문자열 만들기
    def make_correct(p):
        if is_correct(p):
            return p
        left_b, right_b = 0, 0
        u, v = '', ''
        # u, v 나누기
        for i in range(len(p)):
            if p[i] == '(':
                left_b += 1
            elif p[i] == ')':
                right_b += 1
            if left_b == right_b:
                u, v = p[:i+1], p[i+1:]
                break

        if v:
            v = make_correct(v)

        if not is_correct(u):
            new_s = '(' + v + ')'
            for b in u[1:-1]:
                if b == '(':
                    new_s += ')'
                elif b == ')':
                    new_s += '('
            return new_s
        else:
            return u + v

    return make_correct(p)


print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))