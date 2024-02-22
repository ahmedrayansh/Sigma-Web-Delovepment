list_a = [4,-2,8,-5,0]

list_b = sorted(list_a)

zero_index = list_b.index(0)

requirednum = ""

if (0 - list_b[zero_index-1] > list_b[zero_index+1] - 0 ):
    print(list_b[zero_index+1])
else:
    print(list_b[zero_index-1])