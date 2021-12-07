import copy
with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip().split(",") for x in lines]

lyfecycle= [int(n) for n in data[0]]

for i in range(0,80):
    temp = copy.deepcopy(lyfecycle)
    print("dia: "+ str(i))
    for n in range(0,len(temp)):
        lyfecycle[n] -= 1
        if lyfecycle[n] < 0:
            lyfecycle.append(8)
            lyfecycle[n] = 6


print(len(lyfecycle))

