'''
功能：选择排序算法
思想：每一次循环选择最大值或最小值，然后与对应位置上的值交换，每一次循环固定一个位置。
算法时间复杂度：O(n^2)
输入：list 
输出：list
'''
#v0
def select_sort_v0(arr):
    length = len(arr)
    for i in range(length):
        min_ele_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_ele_index]:
                min_ele_index = j
        arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]

    return arr

#v1
'''
优化：同时找最大和最小值
'''
def select_sort_v1(arr):
    length = len(arr)
    for i in range(length):
        min_ele_index = i
        max_ele_index = length-i-1
        for j in range(i+1,length-i):
            if arr[j] < arr[min_ele_index]:
                min_ele_index = j
            if arr[j] > arr[max_ele_index]:
                max_ele_index = j
        arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]
        arr[length-i-1], arr[max_ele_index] = arr[max_ele_index], arr[length-i-1]

    return arr


if __name__=="__main__":
    arr = [5,2,8,1,9,6,7,10,3,25,4,134,234,4324,32,532,432,4234,3216,643,342,5432]
    arr = select_sort_v0(arr)
    print(arr)
