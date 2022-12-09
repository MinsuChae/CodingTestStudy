T = int(input())

def countZero(a,b):
    if a==1:
        return 1
    elif b==0:
        return a
    elif a==2:
        return a*2
    elif b==1:
        return a+1
    elif b < a:
        return a
    else:
        return a*2

str_array = []
for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    result = countZero(arr[0],arr[1])
    str_array.append('#{num} {result}'.format(num=test_case,result = result))

print("\n".join(str_array))