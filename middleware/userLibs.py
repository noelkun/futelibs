class UserLibs():
    def __init__(self, id=0, name=None,doj=None, email=None, password=None):
        self.id=id
        self.email=email
        self.password=password
        self.name=name
        self.doj=doj
        

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
    
    def getDoj(self):
        return self.doj



    def setId(self, id):
        self.id=id

    def setName(self, name):
        self.name=name

    def setEmail(self, email):
        self.email=email

    def setPassword(self, password):
        self.password=password

    def setDoj(self, doj):
        self.doj=doj

    

    def __str__(self):
        return '{},{},{},{},{}'.format(self.id,self.name,self.doj, self.email,self.password)