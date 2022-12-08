T = int(input())
def isPossible(arr):
    count = 0
    for v in arr:
        if v=='1':
            count += 1
    return count%2==1
for test_case in range(1, T + 1):
    arr = list(input())
    result = isPossible(arr)
    result_str = 'yes' if result == True else 'no'
    print('#{num} {result}'.format(num=test_case,result = result))