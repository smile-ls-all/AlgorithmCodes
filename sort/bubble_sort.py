'''
功能：冒泡排序
思想：通过交换相邻两个元素的值，实现一个位置固定。
算法复杂度：O(N^2)
输入：list  arr = [5,2,8,1,9,6,7]
输出：list
'''
#1、初版
def bubble_sort_v0(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#优化版本2
'''
当所有元素有序时，则直接结束排序。
'''
def bubble_sort_v1(arr):
    length = len(arr)
    for i in range(length):
        isSorted = True
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False
        if isSorted:
            break;
    return arr


#优化版本3
'''
当后面某一部分元素有序时，则可以跳过该区域。
v1是v2的特例。
'''
def bubble_sort_v2(arr):
    length = len(arr)
    isSortedIndex = length-1
    for i in range(length):
        isSorted = True
        for j in range(isSortedIndex):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSortedIndex = j
                isSorted = False
        if isSorted:
            break;
        
    return arr


if __name__=="__main__":
    arr = [5,2,8,1,9,6,7,10,3,25,4,134,234,4324,32,532,432,4234,3216,643,342,5432]
    arr = bubble_sort_v2(arr)
    print(arr)


