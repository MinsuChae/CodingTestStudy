T = int(input())

def countRow(array,i, value):
    result = 0
    index = []
    for j in range(len(array[i])):
        if array[i][j] == value:
            result = result + 1
            index.append(j)
    return result, index

def countColumn(array,j, value):
    result = 0
    index = []
    for i in range(len(array)):
        if array[i][j] == value:
            result = result + 1
            index.append(i)
    return result, index

def checkRookRule(array):
    SIZE_N = 8

    for i in range(SIZE_N):
        numOfRook_row, index = countRow(array, i, 'O')
        if numOfRook_row != 1:
            return False
        
        numOfRook_column, index2 = countColumn(array, index[0], 'O')
        if numOfRook_column != 1:
            return False
    return True


for test_case in range(1, T + 1):
    arr = []
    for i in range(8):
        arr.append(list(input()))
    result = checkRookRule(arr)
    result_str = 'yes' if result == True else 'no'
    print('#{num} {result}'.format(num=test_case,result = result_str))

