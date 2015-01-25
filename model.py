class Model:
    def __init__(self):
        self.words = []
        self.page = 0
    def pager(self):
        return self.words[(self.page * 10) : ((self.page+1) * 10)]
    def prev(self):
        if self.page>0:
            self.page -= 1
    def next(self):
        if len(self.words)/10 > self.page:
            self.page += 1
        print('now page is %d' %self.page)
    def query(self, key, dictionary):
        self.page = 0
        self.words = []
        for i in range(len(key),0,-1):
            if key[:i] in dictionary:
                self.words.extend(dictionary[key[:i]])
        if key in dictionary: return
        if len(key)==0: return
        longMatch = ''
        t = key[:]
        while len(t) > 0:
            flag = True
            for i in range(len(t),0,-1):
                if t[:i] in dictionary:
                    longMatch = longMatch + dictionary[t[:i]][0]
                    t = t[i:]
                    flag = False
                    break
            if flag: break
        if ~flag and len(longMatch)>0 : self.words = [longMatch] + self.words


