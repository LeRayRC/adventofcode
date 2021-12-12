with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip() for x in lines]

last_openned = []
error = 0

for line in data:
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
        else:
            if c == ")":
                error += 3
            elif c == "]":
                error += 57
            elif c == "}":
                error += 1197
            elif c == ">":
                error += 25137
            break
    last_openned = []

print("Error: " + str(error))

