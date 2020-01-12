def add_method(*argv):
    sum = 0
    for x in argv:
        try:
            x = float(x)
        except Exception:
            print(x,"is not float")
        else:
            sum += x

    return sum

print(add_method(1,2,3,4,5,6,"ds"))