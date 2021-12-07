import copy
with open('test.txt') as f:
    lines = f.readlines()

data=[x.strip().split(",") for x in lines]

lyfecycle= [int(n) for n in data[0]]

total = 0
data = {}

for x in range(0,10):
    data[x] = lyfecycle.count(x)

print(data)
for d in range(0, 256):
    zeros = data[0]
    data[0] = 0
    for x in range(0,9):
            data[x] = data[x+1]
    data[6] += zeros
    data[8] += zeros


for fish in data:
    total += data[fish]

print(total)
print(data)



