# coding=utf-8

l1 = [1,1,2,3,3]

l2 = [{"a": 3},{"a": 1},{"a": 2},{"a": 1},{"a": 3}]


print list(set(l1))


def deduplicate(l):
    r = []
    tmp = []

    for d in l:
        if d["a"] in tmp:
            continue
        tmp.append(d["a"])
        r.append(d)
    return r


print deduplicate(l2)


def deduplicate1(l):
    r = []
    tmp = []

    for d in l:
        if d["a"] not in tmp:
            tmp.append(d["a"])
            r.append(d)

    return r


print deduplicate1(l2)


r = deduplicate(l2)

print sorted(r, key=lambda d:d["a"])

