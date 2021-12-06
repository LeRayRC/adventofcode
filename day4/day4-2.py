import numpy as np
 
with open('input.txt') as f:
    lines = f.readlines()

bingo=[x.strip() for x in lines]

draws=bingo[0].split(",")

size = 5

matrix_candidate = np.zeros((size,size))
matrix_candidate_marks = np.zeros((size,size))
matrix_winner = np.zeros((size,size))
matrix_winner_marks = np.zeros((size,size))

draw_winner = 1

def check_bingo(matrix_candidate_marks):
    for x in range(0,size):
        if sum(matrix_candidate_marks[x]) == size or sum(matrix_candidate_marks[:,x]) == size:
            return True
    return False

for i in range(1,len(bingo)-1,size+1):
    for j in range(1,size+1):
        row = bingo[i+j].replace("  "," ").split(" ")
        matrix_candidate[j-1] = row
    matrix_candidate_marks = np.zeros((size,size))
    for n in range(0,len(draws)):
        match = np.where(matrix_candidate == float(draws[n]))
        matrix_candidate_marks[match] = 1
        if check_bingo(matrix_candidate_marks):
            if n > draw_winner:
                draw_winner = n
                matrix_winner = matrix_candidate
                matrix_winner_marks = matrix_candidate_marks
                matrix_candidate = np.zeros((size,size))
            break    
print(matrix_winner)
#print(matrix_winner_marks)
unmarked = np.where(matrix_winner_marks == 0.)
print(sum(matrix_winner[unmarked])*float(draws[draw_winner]))
 
