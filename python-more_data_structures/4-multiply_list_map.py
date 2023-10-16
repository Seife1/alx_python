def multiply_list_map(my_list=[], number=0):
    mul_num = map(lambda x: x*number, my_list)
    return list(mul_num)