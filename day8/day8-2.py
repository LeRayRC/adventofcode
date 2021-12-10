with open('input.txt') as f:
    lines = f.readlines()

data=[x.strip().split("|") for x in lines]

output = []

display_ordered = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
display_temp = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}

total = 0

for x in data:
    segments = x[0].strip().split()
    segments.sort(key = len)
    output = x[1].strip().split()
    for signal in segments:
        for digit in signal: 
            display_temp[digit] += 1

    for key in display_temp:
        if display_temp[key] == 4:
            display_ordered["e"] = key
        if display_temp[key] == 6:
            display_ordered["b"] = key
        if display_temp[key] == 9:
            display_ordered["f"] = key

#Ahora se buscan el resto de posiciones en base a lo que se sabe
#Aqui se busca el segundo segmento del 1 
    for signal in segments:
        # Utilizamos el 1 que tiene dos segmentos para sacar el segmento lateral derecho superior
        if len(signal) == 2:
            for digit in signal:
                if display_temp[digit] ==  8:
                    display_ordered["c"] = digit
                    #print("digito c encontrado")
        # Utilizamos el 7 que tiene 3 segmentos para sacar el segmento del medio superior
        if len(signal) == 3:
            for digit in signal:
                #print("digito en c: " + str(display_ordered["c"]))
                if display_temp[digit] ==  8 and display_ordered["a"] == 0 and display_ordered["c"] != digit:
                    display_ordered["a"] = digit
                    #print("digito a encontrado")
        #Utilizamos el 4 que tiene 4 segmentos para sacar el segmento del medio horizontal
        if len(signal) == 4:
            for digit in signal:
                if display_temp[digit] == 7:
                    display_ordered["d"] = digit
        # Utilizamos el 8 que tiene 7 segmentos para sacar el segmento del medio inferior
        if len(signal) == 7:
            for digit in signal:
                if display_temp[digit] == 7 and display_ordered["g"] == 0 and display_ordered["d"] != digit:
                    display_ordered["g"] = digit

    final_value = "" 

    for o in output:
        output_decoded = ""
        
        for digit in o:
            #print("digito utilizado " + str(digit))
            for key in display_ordered:
                if display_ordered[key] == digit:
                    #print("coincidió con " + str(display_ordered[key]))
                    output_decoded += key
        #print(output_decoded)
        if len(output_decoded) == 2:
            final_value += "1"
        elif len(output_decoded) == 4:
            final_value += "4"
        elif len(output_decoded) == 3:
            final_value += "7"
        elif len(output_decoded) == 7:
            final_value += "8"
        elif len(output_decoded) == 6:
            if output_decoded.find("d") == -1:
                final_value += "0"
            elif output_decoded.find("c") == -1:
                final_value += "6"
            else:
                final_value += "9"
        elif len(output_decoded) == 5:
            if output_decoded.find("c") == -1 and output_decoded.find("e") == -1:
                final_value += "5"
            if output_decoded.find("b") == -1 and output_decoded.find("f") == -1:
                final_value += "2"
            elif output_decoded.find("b") == -1 and output_decoded.find("e") == -1:
                final_value += "3"

    total += int(final_value)

    for key in display_temp:
        display_temp[key] = 0
    for key in display_ordered:
        display_ordered[key] = 0

print("Tras una ardua decodificacion el resultado es:")
print("=============================================")
print("=================== " + str(total) + " ==================") 
print("=============================================")

