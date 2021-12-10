with open('test.txt') as f:
    lines = f.readlines()

data=[x.strip().split("|") for x in lines]
signals = []

total = 0

for x in data:
    signals.append(x[1].strip())

for segments in signals:
    patterns = segments.split(" ")
    for pattern in patterns:
        if len(pattern) == 2 or len(pattern) == 3 or len(pattern) == 4 or len(pattern) == 7:
            total += 1

print("Digits 1,4,7 and 8 appear: " + str(total) + " times")
