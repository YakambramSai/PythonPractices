list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]


def diff(list1, list2):
    return (set(list1)-set(list2))

print(diff(list1, list2))

print("2 scenario")
def diff1(list1, list2):
    list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list_dif

print(diff1(list1, list2))

