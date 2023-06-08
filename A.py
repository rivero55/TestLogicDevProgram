list = [12,9,30,'A','M',99,82,'J','N','B']

def sortList(lst):
    string_list = sorted([x for x in lst if isinstance(x, str)])
    number_list = sorted([x for x in lst if isinstance(x, (int, float))])
    return string_list + number_list
order_list = sortList(list)
print(order_list)