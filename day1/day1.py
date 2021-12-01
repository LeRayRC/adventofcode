with open('input.txt') as f:
    lines = f.readlines()

depth_numbers=[int(x.strip()) for x in lines]
increases = 0

for i in range(1,len(depth_numbers)):
    if depth_numbers[i] > depth_numbers[i-1]:
            increases += 1

print("Number of increases: " + str(increases))

number = 0
slide_numbers = []

for i in range(0,len(depth_numbers)-2):
    number = depth_numbers[i] + depth_numbers[i+1] + depth_numbers[i+2]
    slide_numbers.append(number)

slide_increases = 0

for i in range(1,len(slide_numbers)):
    if slide_numbers[i] > slide_numbers[i-1]:
            slide_increases += 1

print("Number of slide increases: " + str(slide_increases))


