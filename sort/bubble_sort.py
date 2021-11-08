'''
功能：冒泡排序
算法复杂度：O(N^2)
输入：list = [5,2,8,1,9,6,7]
输出：list
'''
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__=="__main__":
    arr = [5,2,8,1,9,6,7]
    arr = bubble_sort(arr)
    print(arr)
