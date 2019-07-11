
# g = (x * x for x in range(10))
# for n in g:
#    print(n)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def fab(max):
      n, a, b = 0, 0, 1
      while n < max:
            yield b
            # print b
            a, b = b, a + b
            n = n + 1


for n in fab(5):
    print(n)


a = 'hello'
l=" "
b = 'python'
y=" "
c = '!'
d=''.join([a,l,b,y,c]).strip("h")
print(d)

