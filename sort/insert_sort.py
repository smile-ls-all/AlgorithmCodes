'''
功能：插入排序算法
思想：将第i个位置的值插入到前i个元素组成的有序数列中。
算法时间复杂度：O(n^2)
输入：list 
输出：list
特点：适合有序的数列
'''
#v0
def insert_sort_v0(arr):
    length = len(arr)
    for i in range(length):
        min_ele_index = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[min_ele_index]:
                #每次都交换，可以优化，如v1
                arr[j], arr[min_ele_index] = arr[min_ele_index], arr[j]
                min_ele_index = j
            else:
                break

    return arr

#v1
'''
不用每次交换相邻元素。
'''
def insert_sort_v1(arr):
    length = len(arr)
    for i in range(length):
        key = arr[i]
        flag = 0
        for j in range(i-1,-1,-1):
            if arr[j] > key:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = key
                flag = 1
                break
        if flag == 0:
            arr[0] = key
           
    return arr


if __name__=="__main__":
    arr = [5,2,8,1,9,6,7,10,3,25,4,134,234,4324,32,532,432,4234,3216,643,342,0,5432]
    arr = insert_sort_v1(arr)
    print(arr)

