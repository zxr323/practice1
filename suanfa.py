#徒手写冒泡
def bubble_sort(lis):
    for i in range(1,len(lis)):
        for j in range(0,len(lis)-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis                                 #注意此处要return，否则无返回值
lis = [1,2,3,5,3,4,7,11,9]
print(bubble_sort(lis))


#徒手写快排
lis = [5,3,2,6,8,9,7,1]
def quick_sort(lis,left,right):
    if left<right:
        mid = partition(lis,left,right)
        quick_sort(lis,left,mid-1)
        quick_sort(lis,mid+1,right)
    return lis                                 #注意此处要return，不然print(quick_sort(lis,0,len(lis)-1))无返回值
def partition(lis,left,right):
    while left<right:
        tmp = lis[left]
        while left<right and lis[right]>=tmp:
            right -= 1
        lis[left] = lis[right]
        while left<right and lis[left]<=tmp:   #注意此处要=，不然一直循环
            left += 1
        lis[right] = lis[left]
        lis[left] = tmp
    return left
print(quick_sort(lis,0,len(lis)-1))   
