'''
功能：二分查找
时间复杂度：O(logn)
特点：输入是排序数组。
'''
def binary_search(arr, key):
    length = len(arr)
    begin = 0
    end = length - 1
    while begin <= end:
        mid = begin + (end-begin)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid -1
        elif arr[mid] < key:
            begin = mid+1
    return -1

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    index = binary_search(arr, -1)
    print(index)
        