# an exploration into reversing lists from scratch, with both a normal and recursive approach. this was inspired by a 367 AI lecture where the process of a reversing a list in Datalog came up

def reverse_list(l):
    ret = []
    list_head = l[0]
    while l[0:-1]:
        h = l[-1]
        l = l[0:-1]
        ret.append(h)

    ret.append(list_head)

    return ret


def reverse_list_recurse(l):
    if not l:
        return []
    
    ret = reverse_list_recurse(l[1:])
    ret += [l[0]]

    return ret

i = [1,2,3,4,5,6,7,8,9]
print(reverse_list(i))
print(reverse_list_recurse(i))



