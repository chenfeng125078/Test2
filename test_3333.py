class A:
    def __init__(self):
        print("this is class A")

class C:
    def __init__(self):
        print('this is a new class C')
        print("delete class B")


if __name__ == "main":
    a = A()
    b = B()

