with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip() for x in lines]
risk = 0

length = len(str(data[0]))
lines = len(data)

for i in range(0,lines):
        for d in range(0,length):
            if i == 0:
                string1 = data[i]
                string2 = data[i+1]
                if d == 0:
                    if int(string1[d]) < int(string1[d + 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                elif d == length-1:
                    if int(string1[d]) < int(string1[d - 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                else:
                    if int(string1[d]) < int(string1[d-1]) and int(string1[d]) < int(string1[d+1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
            elif i == lines - 1:
                string1 = data[i]
                string2 = data[i-1]
                if d == 0:
                    if int(string1[d]) < int(string1[d + 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                elif d == length-1:
                    if int(string1[d]) < int(string1[d - 1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
                else:
                    if int(string1[d]) < int(string1[d-1]) and int(string1[d]) < int(string1[d+1]) and int(string1[d]) < int(string2[d]):
                        risk += (1 + int(string1[d]))
            else:
                string1 = data[i]
                string2 = data[i-1]
                string3 = data[i +1]
                if d == 0:
                    if int(string1[d]) < int(string1[d + 1]) and int(string1[d]) < int(string2[d]) and int(string1[d]) < int(string3[d]):
                        risk += (1 + int(string1[d]))
                elif d == length-1:
                    if int(string1[d]) < int(string1[d - 1]) and int(string1[d]) < int(string2[d]) and int(string1[d]) < int(string3[d]):
                        risk += (1 + int(string1[d]))
                else:
                    if int(string1[d]) < int(string1[d-1]) and int(string1[d]) < int(string1[d+1]) and int(string1[d]) < int(string2[d]) and int(string1[d]) < int(string3[d]):
                        risk += (1 + int(string1[d]))        

print("risk is " + str(risk))