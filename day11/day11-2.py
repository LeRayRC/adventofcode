import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip() for x in lines]

length = len(str(data[0]))
lines = len(data)

flashes = 0

map = np.zeros((lines,length))
map_blocked = np.zeros((lines,length))

fig = plt.figure()
ims = []
ims.append([plt.imshow(map, interpolation='none')])

points = []

for i in range(0,lines):
        vector = []
        for d in data[i]:
            vector.append(int(d))
        map[i:] = vector

for step in range(0,1000):
    flashed = 0
    for i in range(0,lines):
        for j in range(0,length):
            map[i][j] += 1
            if map[i][j] > 9:
                map[i][j] = 0
                flashes += 1
                map_blocked[i][j] = 1
                points.append([i,j])

    for point in points:
        i = point[0]
        j = point[1]
        if i+1 < lines:
            if map_blocked[i+1][j] == 0:
                map[i+1][j] += 1
                if map[i+1][j] > 9:
                    map[i+1][j] = 0
                    map_blocked[i+1][j] = 1
                    flashes += 1
                    points.append([i+1,j])
        if i-1 >= 0:
            if map_blocked[i-1][j] == 0:
                map[i-1][j] += 1
                if map[i-1][j] > 9:
                    map[i-1][j] = 0
                    map_blocked[i-1][j] = 1
                    flashes += 1
                    points.append([i-1,j])
        if j+1 < length:
            if map_blocked[i][j+1] == 0:
                map[i][j+1] += 1
                if map[i][j+1] > 9:
                    map[i][j+1] = 0
                    map_blocked[i][j+1] = 1
                    flashes += 1
                    points.append([i,j+1])
        if j-1 >= 0:
            if map_blocked[i][j-1] == 0:
                map[i][j-1] += 1
                if map[i][j-1] > 9:
                    map[i][j-1] = 0
                    map_blocked[i][j-1] = 1
                    flashes += 1
                    points.append([i,j-1])
        if i+1 < lines and j+1 < length:
            if map_blocked[i+1][j+1] == 0:
                map[i+1][j+1] += 1
                if map[i+1][j+1] > 9:
                    map[i+1][j+1] = 0
                    map_blocked[i+1][j+1] = 1
                    flashes += 1
                    points.append([i+1,j+1])
        if i+1 < lines and j-1 >= 0:
            if map_blocked[i+1][j-1] == 0:
                map[i+1][j-1] += 1
                if map[i+1][j-1] > 9:
                    map[i+1][j-1] = 0
                    map_blocked[i+1][j-1] = 1
                    flashes += 1
                    points.append([i+1,j-1])
        if i-1 >= 0 and j+1 < length:
            if map_blocked[i-1][j+1] == 0:
                map[i-1][j+1] += 1
                if map[i-1][j+1] > 9:
                    map[i-1][j+1] = 0
                    map_blocked[i-1][j+1] = 1
                    flashes += 1
                    points.append([i-1,j+1])
        if i-1 >= 0 and j-1 >= 0:
            if map_blocked[i-1][j-1] == 0:
                map[i-1][j-1] += 1
                if map[i-1][j-1] > 9:
                    map[i-1][j-1] = 0
                    map_blocked[i-1][j-1] = 1
                    flashes += 1
                    points.append([i-1,j-1])
        
    for i in range(0,lines):
        for j in range(0,length):
            if map[i][j] == 0:
                flashed += 1
    if flashed == 100:
        print("All flashed at step " + str(step+1))
        break

    ims.append([plt.imshow(map, interpolation='none')])
    map_blocked = np.zeros((lines,length))
    points = []
    print("========================")
    print("Step " + str(step+1))
    print(map)
    print(map_blocked)
    print("Flashes " + str(flashes))
    print("========================")

ani = animation.ArtistAnimation(fig, ims, interval=1000, blit=True,
                                repeat_delay=100)

plt.show()
