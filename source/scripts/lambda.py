map(lambda x: x + 2, [range(10)])
mymap = map(lambda x: x + 2, [range(10)])
mymap
mymap.next()
[mymap]
*mymap
list(mymap)
map(lambda x: x+2, [x for x in range(10)])
list(map(lambda x: x+2, [x for x in range(10)]))
list(map(x+2, [x for x in range(10)]))
list(map((x+2), [x for x in range(10)]))
list(map(*(x+2), [x for x in range(10)]))
add_two(x):
def add_two(x):
    return x + 2
list(map(lambda x: x+2, [x for x in range(10)]))
list(map(add_two(x), [x for x in range(10)]))
list(map(add_two, [x for x in range(10)]))
def mod_two(x):
    return x % 2
list(map(mod_two, [x for x in range(10)]))
list(map(lambda x: x % 2, [x for x in range(10)]))
single_digits = [x for x in range(10)]
single_digits
lambda x: x + 2
dir()
lambda x: x + 2 ; dir()
lambda x: x + 2
dir()
dir(__main__)
%history -f lambda001.py
