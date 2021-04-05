class Math:

    @staticmethod  # not change/stay same
    def add9(x):
        return x + 9

    @staticmethod
    def add50(x):
        return x + 50

    @staticmethod
    def pr():
        print("run")


Math.pr()
print(Math.add9(5))
