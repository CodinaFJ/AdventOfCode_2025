def search_for_max_idx(digits):
    max = 0
    max_digit = 0
    for i, digit in enumerate(digits):
        if digit > max:
            max_digit = i
            max = digit
    return max_digit


res = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        digits = [int(d) for d in line]
        print(digits)
        n = 0
        for i in range(12):
            if i < 11:
                ni = search_for_max_idx(digits[:-11 + i])
            else:
                ni = search_for_max_idx(digits)
            n += digits[ni] * (10 ** (11 - i))
            digits = digits[ni + 1:]
        print(n)
        res += n
    print("result:", res)
