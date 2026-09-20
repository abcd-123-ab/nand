def knapsackrec(w,val,wt,n):
    if n==0 or w==0:
        return 0
    pick=0

    if wt[n-1]<=w:
        pick=val[n-1]+knapsackrec(w-wt[n-1],val,wt,n-1)
    notpick=knapsackrec(w,val,wt,n-1)
    return max (pick,notpick)


def knapsack(w,val,wt):
    n=len(val)
    return knapsackrec(w,val,wt,n)

val=[1,7,11]
wt=[1,2,3]
w=5
print(knapsack(w,val,wt))