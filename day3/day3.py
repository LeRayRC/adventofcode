import math
# Challenge 1

with open('input.txt') as f:
    lines = f.readlines()

rates=[x.strip() for x in lines]

ones = [0] * len(rates[0])
zeros = [0] * len(rates[0])

for i in range(0,len(rates)):
    for c in range(0,len(rates[i])):
        if rates[i][c] == "1":
            ones[c] += 1
        else:
            zeros[c] += 1

epsilon_list = [0] * len(rates[0])
gamma_list = [0] * len(rates[0])

for n in range(0,len(ones)):
    if ones[n] > zeros[n]:
        epsilon_list[n] = 1
        gamma_list[n] = 0
    else:
        epsilon_list[n] = 0
        gamma_list[n] = 1

epsilon_rate = 0
gamma_rate = 0

for n in range(0,len(epsilon_list)):
    epsilon_rate += epsilon_list[n] * pow(2,len(epsilon_list)-1-n)
    gamma_rate += gamma_list[n] * pow(2,len(epsilon_list)-1-n)

print(gamma_rate)
print(epsilon_rate)
print(gamma_rate * epsilon_rate)

# Challenge 2 

def filter(rates,index,priority):
    one_begin = []
    zero_begin = []
    chosen_list = rates
    for i in range(0,len(rates)):
        if rates[i][index] == "1":
            one_begin.append(rates[i])
        else:
            zero_begin.append(rates[i])
    if len(one_begin) > len(zero_begin):
        if priority == "high" and len(one_begin) > 0:
            chosen_list = one_begin
        elif priority == "low" and len(zero_begin) > 0:
            chosen_list = zero_begin
    elif len(zero_begin) > len(one_begin):
        if priority == "high" and len(zero_begin) > 0:
            chosen_list = zero_begin
        elif priority == "low" and len(one_begin) > 0:
            chosen_list = one_begin
    elif len(zero_begin) == len(one_begin):
        if priority == "high":
            chosen_list = one_begin
        elif priority == "low":
            chosen_list = zero_begin
    if index == len(rates[0])-1:
        return chosen_list[0]
    else:
        return filter(chosen_list,index+1,priority)


oxygen = filter(rates,0,"high")
c02 = filter(rates,0,"low")
oxygen_rate = 0
c02_rate = 0

print(oxygen)
print(c02)

for n in range(0,len(oxygen)):
    oxygen_rate += int(oxygen[n]) * pow(2,len(oxygen)-1-n)
    c02_rate += int(c02[n]) * pow(2,len(c02)-1-n)

print(oxygen_rate)
print(c02_rate)
print(oxygen_rate*c02_rate)

