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

def get_all_div_num_for_size(size):
    divs = []
    for x in range(1, size):
        if size % x != 0:
            continue
        aux = 0
        for i in range(size):
            if i % x != 0:
                continue
            aux += 10**i
        divs.append(aux)
    print("interval", divs)
    return(divs)

def resolve(min, max):
    print(min, max)
    res = 0
    tagged_list = []
    for div in get_all_div_num_for_size(get_num_size(min)):
        dif = max//div - min//div
        for i in range(dif):
            aux = (max//div - i) * div
            if tagged_list.count(aux) > 0:
                continue
            print("\tBingo", aux)
            tagged_list.append(aux)
            res += aux
        if min%div == 0:
            aux = min
            if tagged_list.count(aux) > 0:
                continue
            print ("\tBingo", aux)
            tagged_list.append(aux)
            res += aux
    return res


strs  =[[]]
with open("input.txt") as f:
    for line in f:
        line.strip()
        strs = line.split(",")

res = 0
for line in strs:
    nums = [0, 0]
    strs = line.split("-")
    nums[0] = int(strs[0])
    nums[1] = int(strs[1])
    if get_num_size(nums[0]) != get_num_size(nums[1]):
        print("\tNeeds correction")
        res += resolve(nums[0], get_max_num_by_size(get_num_size(nums[0])))
        res += resolve(get_min_num_by_size(get_num_size(nums[0])), nums[1]) 
    else:
        res += resolve(nums[0], nums[1])
        
print("Result", res)


