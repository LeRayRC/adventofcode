with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip() for x in lines]

last_openned = []

scores = []
lines_fixed = 0

for line in data:
    fail_detected = False
    for c in line:
        if c == "]" and last_openned[len(last_openned)-1] == "[":
            last_openned.pop(len(last_openned)-1)
        elif c == "}" and last_openned[len(last_openned)-1] == "{":
            last_openned.pop(len(last_openned)-1)
        elif c == ">" and last_openned[len(last_openned)-1] == "<":
            last_openned.pop(len(last_openned)-1)
        elif c == ")" and last_openned[len(last_openned)-1] == "(":
            last_openned.pop(len(last_openned)-1)
        elif c == "(" or c == "{" or c == "[" or c == "<":
            last_openned.append(c)
        elif not fail_detected:
            fail_detected = True
            break
    if not fail_detected:
        score_temp = 0
        for s in range(len(last_openned)-1,-1,-1):
            if last_openned[s] == "(":
                score_temp = (score_temp * 5) + 1
            elif last_openned[s] == "[":
                score_temp = (score_temp * 5) + 2
            elif last_openned[s] == "{":
                score_temp = (score_temp * 5) + 3
            elif last_openned[s] == "<":
                score_temp = (score_temp * 5) + 4
            last_openned.pop(s)
        lines_fixed += 1
        scores.append(score_temp)
    last_openned = []

scores.sort()
middle = int((len(scores)-3) / 2 + 1)
print("Middle value " + str(scores[middle]))