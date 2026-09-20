def knapsackRec(W, val, wt, n):
    if n == 0 or W == 0:
        return 0
    pick = 0
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)
        print("picked:",pick)
    notPick = knapsackRec(W, val, wt, n - 1)
    print("not picked:",notPick)
    return max(pick, notPick)
def knapsack(W, val, wt):
    n = len(val)
    return knapsackRec(W, val, wt, n)

val = [1, 7, 11]
wt = [1, 2, 3]
W = 5
result = knapsack(W, val, wt)
print("result:",result)