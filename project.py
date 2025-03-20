class SAII:
    def __init__(self, name, creator, inspire):
        self.SAII = name
        self.Brian = creator
        self.JAVIS = inspire
        
    def fname(self, fname):
        return  "Hello I am {}, My full name is {}".format(self.SAII, fname)
    
    def also(self):
        print("I was inspired by {}".format(self.JAVIS))
        print("my creator is {}".format(self.Brian))

introd = SAII("SAII", "Brian", "JAVIS from Iron man")

print(introd.fname("San Anonymous Artificial Intelligence"))
introd.also()