def fractional_knapsack(capacity,weight,values,name):
    n=len(values)
    items=[]

    for i in range(n):
        ratio=values[i]/weight[i]
        items.append((ratio,values[i],weight[i],name[i]))
        items.sort(reverse=True)
        total_value=0.0

    for ratio,value,weight,name in items:
        if capacity>=weight:
            capacity-=weight
            total_value+=value
            print(name,"=>weight-",capacity,",value-",value)
        else:
            remaining=ratio*capacity
            total_value+=ratio*capacity
            print(name,"->weight  - ", capacity, " value -",remaining)
            print(f"\n remaining item:{name}->weight:{weight-capacity},remaoning values:{value-remaining}\n")
            break
        return total_value

name=["silver","platium","gold"]
values=[100,60,120]
weight=[20,10,30]
capacity=50

result=fractional_knapsack(capacity,weight,values,name)
print("total capacity",capacity)
print("result",result)