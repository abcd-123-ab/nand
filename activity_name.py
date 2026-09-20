def activity_selection(start,finish):
    activities = list(zip(start,finish))
    print("-"*50)
    print("Activities:" , activities)

    activities.sort(key = lambda x:x[1])

    selected = []
    end_values = 0

    for s,f in activities:
        print("-"*50)

        print("start :",s)
        print("end :",f)
        print("Before selected :" , selected)

        if s >= end_values:
            selected.append((s,f))
            print("After selection :" , selected)
            end_values = f
    
    return selected
start = [1 , 3 , 0 , 5 , 8 , 5]
finish = [2 , 4 , 6 , 7 , 9 , 9]
print("start array:",start)
print("finish array:",finish)
result = activity_selection(start , finish)
print("-"*50)
print("activity selection: " , result)