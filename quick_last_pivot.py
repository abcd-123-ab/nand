def quick_sort(arr,low,high):
    if low<high:
        pivot=patition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

def patition(arr,low,high):
    p=arr[high]
    print(p)
    i=low
    j=high-1


    while True:
        print(arr)

        while i<=j and arr[i]<=p:
            i+=1

        while i<=j and arr[j]>=p:
            j-=1

        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]

        else:
            break

    arr[i],arr[high] = arr[high],arr[i]
    return i


arr=[5,0,7,1,3]
quick_sort(arr,0,len(arr)-1)
print(arr)