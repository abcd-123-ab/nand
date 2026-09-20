def fractional_knapsack(capacity, weight, values):
    n = len(values)
    items = []
    for i in range(n):
        ratio = values[i] / weight[i]
        print("-"*50)
        print("Ratio:" , ratio)
        items.append((ratio, values[i], weight[i]))

    items.sort(reverse=True)
    print("-"*50)
    print("Sorted items :",items)
    total_value = 0.0

    for ratio, value, weight in items:
        if capacity >= weight:
            print("-"*50)
            print("Before add capacity:" , capacity)
            print("values:" , values)
            print("weight:", weight)

            print(f"after added capacity : {capacity} - {weight}:",capacity)
            capacity -= weight
            total_value += value
            print("-"*50)
            print("total values:",total_value)
        else:
            total_value += ratio * capacity
            print("-"*50)
            print(f"after added capacity : {capacity} - {weight}:",capacity)
            print("Before add capacity:" , capacity)
            print("total values:",total_value)
            break
    return total_value
values = [100, 60, 120]
weight = [20, 10, 30]
capacity = 50
print("values:" , values)
print("weight:", weight)
print("Before add capacity:" , capacity)
print("-"*50)

result = fractional_knapsack(capacity, weight, values)
print("-"*50)
print("Maximum value in knapsack =", round(result, 2))