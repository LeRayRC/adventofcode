with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip().split(",") for x in lines]

crabs = [int(n) for n in data[0]]
fuel_cost = 10000000000000
fuel_cost_candidate = 0

for c in range(0,max(crabs)):
    fuel_cost_candidate = 0
    for i in range(0,len(crabs)):
        fuel_cost_candidate += abs(crabs[i] - c)
    if fuel_cost_candidate < fuel_cost:
        fuel_cost = 0
        fuel_cost += fuel_cost_candidate

print(fuel_cost)
print(crabs)