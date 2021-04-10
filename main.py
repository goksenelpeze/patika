def flattenList(lst):
    flatten_lst = []
    for i in lst:
        if type(i) == list:
            l = flattenList(i)
            flatten_lst.extend(l)
        else:
            flatten_lst.append(i)
    return flatten_lst


def reverseList(lst):
    reversedList = []
    for i in lst[::-1]:
        if type(i) == list:
            l = reverseList(i)
            reversedList.append(l)
        else:
            reversedList.append(i)

    return reversedList


lst = [5, [1, [[1,2],2]], [3, 4], [5, 6, 7]]

print(flattenList(lst))

print(reverseList(lst))