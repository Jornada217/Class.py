
class grandma():
    def __init__(self, gname):
        self.gname = gname

    def granname(self):
        return self.gname

class mom():
    def __init__(self, mname):
        self.mname = mname


    def momname(self):
        return self.mname

class son(grandma, mom):
    def __init__(self, gname, mname, sname):
        mom.__init__(self, mname)
        grandma.__init__(self, gname)
        self.sname = sname


    def sonname(self):
        return print('Joao')

# j = son('Angelina', 'Dirce', 'Joao')
# print(j.granname(), j.momname(), j.sonname())

print(son().sonname())