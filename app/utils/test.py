class test:
    def __init__(self):
        self.a = '123'

t = 'a'
test = test()
print getattr(test, t)
