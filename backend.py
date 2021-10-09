import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS inventory(id INTEGER PRIMARY KEY,product text ,company text,Mfgyear INTEGER, pid INTEGER )")
        self.conn.commit()

    def insert(self,product,company,Mfgyear,pid):
        self.cur.execute("INSERT into inventory VALUES (NULL,?,?,?,?)",(product,company,Mfgyear,pid))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM inventory")
        rows=self.cur.fetchall()
        return rows

    def search(self,product="",company="",Mfgyear="",pid=""):
        self.cur.execute("SELECT * FROM inventory where product=? OR company=? OR Mfgyear=? OR pid=?",(product,company,Mfgyear,pid))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM inventory where id =?",(id,))
        self.conn.commit()

    def update(self,id,company,product,Mfgyear,pid):
        self.cur.execute("UPDATE inventory SET produuct=?,company=?,Mfgyear=?,pid=? WHERE id=?",(product,company,Mfgyear,pid,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
