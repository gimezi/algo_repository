str = input()
ks = []
qs = []

temp = ''

for i in range(len(str)):
    letter = str[i]

    # 여는 괄호일 때
    if letter == '(':
        k = int(str[i - 1])
        ks.append(k)
        temp = temp[:len(temp) - 1]
        if temp != '':
            qs.append(temp)
            temp = ''

    # 닫는 괄호일 때
    elif letter == ')':
        if temp != '':
            qs.append(temp)
            temp = ''


    # 그냥 문자일 때
    else:
        temp += letter
    
if temp != '':
    qs.append(temp)

print(ks)
print(qs)

result = ''
while qs or ks:
    print(qs, ks)
    if qs:
        q = qs.pop()
        if len(ks):
            k = ks.pop()
            result = k * (q + result)
        else:
            result = q + result
    
    # q가 다 비었고, k만 남았을때
    else:
        k = ks.pop()
        result = k * result

print(result)
print(len(result))

    
        
    