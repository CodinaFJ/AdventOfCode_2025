def get_min_num_by_size(size):
    return(10 ** size)

def get_max_num_by_size(size):
    return((10 ** (size)) - 1)

def get_num_size(num):
    res = 0
    while num > 0:
        num = num // 10
        res += 1
    return(res)


def get_div_num(nbr):
    res = 1
    num = nbr
    while num > 0:
        num = num // 10
        res *= 10
    res = res + 1
    return(res)

strs  =[[]]
with open("input.txt") as f:
    for line in f:
        line.strip()
        strs = line.split(",")

res = 0
for line in strs:
    print(line)
    nums = [0, 0]
    strs = line.split("-")
    nums[0] = int(strs[0])
    nums[1] = int(strs[1])
    if get_num_size(nums[0]) % 2 != 0 and get_num_size(nums[1]) % 2 != 0:
        print("\tBoth odds - SKIP")
        continue
    if get_num_size(nums[0]) != get_num_size(nums[1]):
        print("\tNeeds correction")
        if get_num_size(nums[0]) % 2 != 0:
            nums[0] = get_min_num_by_size(get_num_size(nums[0]))
        elif get_num_size(nums[1]) % 2 != 0:
            nums[1] = get_max_num_by_size(get_num_size(nums[0]))
        print("\t", nums[0], "-", nums[1])

    div = 10**(get_num_size(nums[0])//2) + 1
    print("\tDivided by:", div)
    dif = nums[1]//div - nums[0]//div
    for i in range(dif):
        res += (nums[1]//div - i) * div
    if nums[0]%div == 0:
        res += nums[0]
        
print("Result", res)



