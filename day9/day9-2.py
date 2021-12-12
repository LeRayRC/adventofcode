import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip() for x in lines]
risk = 0

length = len(str(data[0]))
lines = len(data)

lows = []
basins = []

map = np.zeros((lines,length))
map_basins = np.zeros((lines,length))
for i in range(0,lines):
        vector = []
        for d in data[i]:
            vector.append(int(d))
        map[i:] = vector

for i in range(0,lines):
    for j in range(0,length):
        if map[i][j] == 9:
            map_basins[i][j] = 500
        else:
            map_basins[i][j] = 999

fig = plt.figure()
ims = []
ims.append([plt.imshow(map_basins, interpolation='none')])



def expand(low):
    lows = [low]
    size = 1
    for low in lows:
        #print(low[0])
        if low[0] + 1 < lines:
            if map_basins[low[0]+1][low[1]] == 999:
                 map_basins[low[0]+1][low[1]] = 1
                 lows.append([low[0]+1,low[1]])
                 size += 1
        if low[0] - 1 >= 0:
            if map_basins[low[0]-1][low[1]] == 999:
                 map_basins[low[0]-1][low[1]] = 1
                 lows.append([low[0]-1,low[1]])
                 size += 1
        if low[1] - 1 >= 0:
            if map_basins[low[0]][low[1]-1] == 999:
                 map_basins[low[0]][low[1]-1] = 1
                 lows.append([low[0],low[1]-1])
                 size += 1
        if low[1] + 1 < length:
            if map_basins[low[0]][low[1]+1] == 999:
                 map_basins[low[0]][low[1]+1] = 1
                 lows.append([low[0],low[1]+1])
                 size += 1
    ims.append([plt.imshow(map_basins, interpolation='none')])
    return size


for i in range(0,lines):
        for d in range(0,length):
            if i == 0:
                string1 = data[i]
                string2 = data[i+1]
                if d == 0:
                    if int(string1[d]) < int(string1[d + 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
                elif d == length-1:
                    if int(string1[d]) < int(string1[d - 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
                else:
                    if int(string1[d]) < int(string1[d-1]) and int(string1[d]) < int(string1[d+1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
            elif i == lines - 1:
                string1 = data[i]
                string2 = data[i-1]
                if d == 0:
                    if int(string1[d]) < int(string1[d + 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
                elif d == length-1:
                    if int(string1[d]) < int(string1[d - 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
                else:
                    if int(string1[d]) < int(string1[d-1]) and int(string1[d]) < int(string1[d+1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
            else:
                string1 = data[i]
                string2 = data[i-1]
                string3 = data[i +1]
                if d == 0:
                    if int(string1[d]) < int(string1[d + 1]) and int(string1[d]) < int(string2[d]) and int(string1[d]) < int(string3[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
                elif d == length-1:
                    if int(string1[d]) < int(string1[d - 1]) and int(string1[d]) < int(string2[d]) and int(string1[d]) < int(string3[d]):
                        risk += (1 + int(string1[d]))
                        map_basins[i][d] = 1
                        lows.append([i,d])
                else:
                    if int(string1[d]) < int(string1[d-1]) and int(string1[d]) < int(string1[d+1]) and int(string1[d]) < int(string2[d]) and int(string1[d]) < int(string3[d]):
                        risk += (1 + int(string1[d]))    
                        map_basins[i][d] = 1
                        lows.append([i,d])
print("risk is " + str(risk))


for low in lows:
    size_basin = expand(low)
    basins.append(size_basin)

basins.sort(reverse=True)
print("Top 3 Basin values: " + str(basins[0]) + " , " + str(basins[1]) + " , " + str(basins[2]))
print(basins[0] * basins[1] * basins[2])

ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=100)

plt.show()