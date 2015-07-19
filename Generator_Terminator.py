__author__ = 'armen'
def list_generator(n_elements, min_value, max_value):
    import random
    generated_list = []
    for i in range(0, n_elements):
        generated_list.append(random.randint (min_value, max_value))
    return generated_list




a = list_generator(2,0,10)
print a