def zhujie(a:int,b:float)-> float :
      c=2
      return  a+b+c


v=zhujie(4,5)
print(dir(zhujie),zhujie.__annotations__)
print(v,zhujie.__code__,zhujie.__code__.co_varnames,zhujie.__code__.co_freevars)
print(dir(v))

