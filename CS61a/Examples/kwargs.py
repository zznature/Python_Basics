

def f(*args, **kwargs):
    print(args)
    print(*args)
    # print(tuple(*args))
    print(kwargs)
    print(*kwargs)
    #print(**kwargs) 


f('Paris', 'Monday', 100, Italy=2, French=3, Potato=4)

# arguments should be a tuple
#'*' changes into tuple
#'**'' changes into dictionary
