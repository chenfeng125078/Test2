class A:
    def __init__(self):
        print("this is second file A class")
        print("no change")


class C:
    def __init__(self):
        print("delete class B")
        print("add a new class C")


if __name__ == '__main__':
    printer_1 = A()
    printer_2 = B()
