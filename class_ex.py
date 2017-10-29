class One():
    def __init__(self):
        self.name = "Haha"
        print("This is One.")

    def one(self):
        print(self.name)

class Two(One):
    def __init__(self):
        super()
        self.__name = "Hehe"
        print("This is Two.")

    def two(self):
        print(self.__name)

class Three(Two):
    def __init__(self):
        #ex = super(Three)
        super()#.__init__()
        self.__name = "Huihui"
        print("This is Three.")

    def three(self):
        print(self.__name)