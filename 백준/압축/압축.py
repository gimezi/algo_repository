s = input().strip()

def fun(s, idx):
    result = 0  # 결과 문자열의 길이
    while idx < len(s):
        now = s[idx]

        if now == ')':
            return result, idx + 1  # 괄호 닫히면 현재 길이, 위치 반환
        
        if now.isdigit():  # 숫자면
            # 다음 문자가 여는 괄호인지 확인
            if idx + 1 < len(s) and s[idx + 1] == '(': 
                num = int(now)
                inner_len, next_idx = fun(s, idx + 2)
                result += num * inner_len
                idx = next_idx
            else:
                result += 1
                idx += 1
        else:
            result += 1
            idx += 1

    return result, idx

length, _ = fun(s, 0)
print(length)