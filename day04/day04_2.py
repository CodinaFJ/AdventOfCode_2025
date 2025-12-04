def is_accesible(matrix, i, j):
    hits = 0
    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            if abs(m) + abs(n) == 0 :
                continue
            if i + m < 0 or i + m >= len(matrix) or j + n < 0 or j + n >= len(matrix[0]):
                continue
            hits = hits + 1 if matrix[i+m][j+n] == '@' or matrix[i+m][j+n] == 'X' else hits
    return False if hits >= 4 else True


with open("input.txt") as f:
    matrix = [list(line.rstrip("\n")) for line in f]

res = 0
res_prev = 0
changed = True
while True: 
    for i,line in enumerate(matrix):
        for j,char in enumerate(line):
            if char == '@':
                if is_accesible(matrix,i,j):
                    matrix[i][j] = '.'
                    res += 1
    if res == res_prev:
        break
    res_prev = res

print("RESULT", res)
