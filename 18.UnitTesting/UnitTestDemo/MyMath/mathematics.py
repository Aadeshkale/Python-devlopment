class Maths(object):

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def div(self, x, y):
        return x // y



if __name__ == '__main__':
    m = Maths()
    print(m.add(2, 3))
    print(m.div(5, 2))
