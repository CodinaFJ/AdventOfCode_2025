
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
        n1 = search_for_max_idx(digits[:-1])
        n2 = search_for_max_idx(digits[n1 + 1:])
        n = digits[n1]*10 + digits[n2+n1+1]
        print(n)
        res += n
    print("result:", res)
