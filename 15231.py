T = int(input())

lower_list = []
upper_list = []

def init_depth():
    for i in range(0,63):
        lower_list.append(2**i)
        upper_list.append((2**(i+1)))
        
init_depth()

def depth(x):
    for i in range(len(lower_list)):
        if lower_list[i] <= x < upper_list[i]:
            return i+1, x <(lower_list[i]+upper_list[i])//2
            
def cal_distance(n, v):
    tree_depth,tree_is_diff_nodes = depth(n)
    if v==1 or n<=2:
        return tree_depth - 1
    else:
        now_depth, now_is_left = depth(v)
        return now_depth - 2 + tree_depth - (tree_is_diff_nodes&now_is_left)
        
str_array = []
for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    result = cal_distance(arr[0],arr[1])
    str_array.append('#{num} {result}'.format(num=test_case,result = result))
print("\n".join(str_array))