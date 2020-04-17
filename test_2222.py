class A:
    def __init__(self):
        print("this is second file A class")
        print("no change")


class B:
    def __init__(self):
        print("this is second file B class")
        print("no change")


if __name__ == '__main__':
    printer_1 = A()
    printer_2 = B()
