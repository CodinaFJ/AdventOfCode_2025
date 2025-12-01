aoc_input = []

with open("data.txt") as f:
    for line in f:
        line = line.strip()
        
        letter = line[0]
        number = int(line[1:])

        if letter == "L":
            aoc_input.append(-(number%100))
        elif letter == "R":
            aoc_input.append(number%100)
        else:
            raise ValueError("Wrong input")

#print(aoc_input)        

number = 50
res = 0
for n in aoc_input:
    number += n

    if number > 99 :
        number -= 100
    elif number < 0 :
        number += 100

    if number == 0 :
        res += 1

print(res)
