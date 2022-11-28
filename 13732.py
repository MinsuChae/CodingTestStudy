T = int(input())

def countRow(array,i, value):
    index = []
    for j in range(len(array[i])):
        if array[i][j] == value:
            index.append(j)
    return index


def countColumn(array,j, value):
    index = []
    for i in range(len(array)):
        if array[i][j] == value:
            index.append(i)
    return index

def checkSquareRule(array,n):
    startRow = None
    index = None
    squire = 0
    
    i = 0
    while i < n:
        index = countRow(array,i,'#')
        if len(index) > 0:
            startRow = i
        else:
            i = i + 1
            continue
            
        length = len(index)
        for j in range(1, length):
            if index[j-1]+1 != index[j]:
                return False
        for j in index:
            tmp_index = countColumn(array,j,'#')
            tmp_length = len(tmp_index)
            if tmp_length != length:
                return False

            for k in range(1, tmp_length):
                if tmp_index[k-1]+1 != tmp_index[k]:
                    return False
        i = i + length
        squire = squire + 1
    return squire == 1

for test_case in range(1, T + 1):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(input()))
    
    result = checkSquareRule(arr, n)
    result_str = 'yes' if result == True else 'no'
    print('#{num} {result}'.format(num=test_case,result = result_str))
    