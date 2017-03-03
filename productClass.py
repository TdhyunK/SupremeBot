class productClass:
    def __init__(self, url, size = None):
        self.url = url
        self.size = size
        print "Created product Obj"


    def getURL(self):
        return self.url;

    def getSize(self):
        return self.size