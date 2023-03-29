class Writer:
    def __init__(self,server,port,username,database,password):
        self.server=server
        self.port=port
        self.username=username
        self.database=database
        self.password=password
    def writeToFile(self):
        f = open("Oracle.txt", "w")
        f.write(self.server+"\n")
        f.write(self.port+"\n")
        f.write(self.username+"\n")
        f.write(self.database+"\n")
        f.write(self.password+"\n")
        f.close()
    def readFile(self):
        try:
            f = open("Oracle.txt", "r")
            server=f.readline()[:-1]
            port=f.readline()[:-1]
            username=f.readline()[:-1]
            database=f.readline()[:-1]
            password=f.readline()[:-1]
            f.close()
            return (server,port,username,database,password)
        except:
            return None

w=Writer(port="11",server="local",database="Xe",password="password",username="us")
w.writeToFile()
print(w.readFile())