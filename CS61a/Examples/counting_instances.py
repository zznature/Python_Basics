class C():

    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


print(__name__)

if __name__ == "__main__":
    x = C()
    print(x.counter)
    print("Number of instances: : " + str(C.counter))
    y = C()
    print(y.counter)
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
