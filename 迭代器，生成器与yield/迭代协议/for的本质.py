

a = (1,2,3,4)

b = iter(a)

while 1:
    try:
        print(b.__next__())
    except StopIteration:
        break

#原理就是上面这个   本质是个迭代器
for b in a :
    print(b)