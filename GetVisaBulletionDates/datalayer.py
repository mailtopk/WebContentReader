import sqlite3

class databaselayer :
    
    name = "visa_db.db"
    
    def getConn(self):
        return sqlite3.connect(self.name)
    
    def getCurrsor():
        sqlite3.Cursor()
    
    def closeDB(self):
        curr = self.getCurrsor()
        curr.close()


    def getLatestReleaseDate(self):
        return self.getCurrsor().execute('SELECT TOP 1 ORDER BY ID DESC')
    
