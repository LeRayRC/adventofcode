import numpy


import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

size = 1000
data=[x.strip() for x in lines] 
matrix = np.zeros((size,size))
#Poner a False para el primer desafio
diagonales = True
countDiagonales = 0

for i in range(0,len(data)):
    coordinates = data[i].split("->")
    point_begin=[int(i) for i in coordinates[0].replace(" ","").split(",")]
    point_end=[int(i) for i in coordinates[1].replace(" ","").split(",")]
    if point_end[0] == point_begin[0]:
        if point_end[1] > point_begin[1]:
            for x in range(point_begin[1],point_end[1]+1):
                matrix[x][point_end[0]] += 1
        else:
            for x in range(point_end[1],point_begin[1]+1):
                matrix[x][point_end[0]] += 1
    elif point_end[1] == point_begin[1]:
        if point_end[0] > point_begin[0]:
            for x in range(point_begin[0],point_end[0]+1):
                matrix[point_end[1]][x] += 1
        else:
            for x in range(point_end[0],point_begin[0]+1):
                matrix[point_end[1]][x] += 1   
    elif diagonales:
        countDiagonales += 1
        if point_end[0] > point_begin[0]:
            if point_end[1] > point_begin[1]:
                for x in range(0,point_end[0]-point_begin[0]+1):
                    matrix[point_begin[1]+x][point_begin[0]+x] += 1
            else:
                for x in range(0,point_end[0]-point_begin[0]+1):
                    matrix[point_begin[1]-x][point_begin[0]+x] += 1
        else:
            if point_end[1] > point_begin[1]:
                for x in range(0,point_begin[0]-point_end[0]+1):
                    matrix[point_begin[1]+x][point_begin[0]-x] += 1
            else:
                for x in range(0,point_begin[0]-point_end[0]+1):
                    matrix[point_begin[1]-x][point_begin[0]-x] += 1

if diagonales: print("Total diagonales: " + str(countDiagonales))
print(len(matrix[np.where(matrix >= 2.)]))
print(matrix)
    