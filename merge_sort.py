def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]

    sortedleft=merge_sort(lefthalf)
    sortedright=merge_sort(righthalf)

    return merge(sortedleft,sortedright)

def merge(left,right):
    result=[]
    i=j=0

    while(i<len(left) and j<len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

array=[1,33,5,99,0]
print("orignal array",array)
ans=merge_sort(array)
print("sorted array",ans)            