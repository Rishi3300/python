a=50
def show():
    a=10
    print("local variable a",a)
    x=globals()['a']
    print("X",x)
show()
print(" global variable a:",a)


