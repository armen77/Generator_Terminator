#----------------------
def list_generator(n_elements, min_value, max_value):
    import random
    generated_list = []
    for i in range(0, n_elements):
        generated_list.append(random.randint(min_value, max_value))
    return generated_list
#----------------------
def list_terminator(current_list, summ):
    n_elements = len(current_list)
    for cnt_1 in range(0, n_elements - 2):
        for cnt_2 in range(cnt_1 + 1, n_elements - 1):
            if current_list[cnt_1] + current_list[cnt_2] == summ:
                print current_list[cnt_1], current_list[cnt_2]
    return 0
#----------------------
a = list_generator(11,0,10)
print a
b = list_terminator(a, 14)


