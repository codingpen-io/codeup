def sub_lists(l):
    lists = [[]]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists

    return lists[1:]


# driver code
l1 = [2, 3, 1, 2, 1]
print(sub_lists(l1))
