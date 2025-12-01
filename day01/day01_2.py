aoc_input = []
res = 0
num = 50

with open("data.txt") as f:
    for line in f:
        line = line.strip()
        
        letter = line[0]
        number = int(line[1:])

        prev_num = num
        res += number // 100
        if letter == "L":
            num -= number%100
        elif letter == "R":
            num += number%100
        else:
            raise ValueError("Wrong input")

        if num == 100 :
            num = 0
        elif num > 99 :
            res += 1
            num -= 100
        elif num < 0 :
            if prev_num != 0 :
                res += 1
            num += 100

        if num == 0 :
            res += 1

        #print("after", letter, number, "started at", prev_num, "end at", num, "res", res)

        prev_num = num

print(res)
