import sqlite3
class Database:
    def __init__(self,address):
        self.con=sqlite3.connect(address)
        self.cur=self.con.cursor()
        self.cur.execute('''create table if not exists courses (id integer primary key,
                         name text,lname text,course text, pword integer primary key)''')
        self.con.commit()
    def add(self,name,lname,course,pword):
        self.cur.execute('insert into courses values (NULL,?,?,?,?)',(name,lname,course,pword))
        self.con.commit()
    def fetch(self):
        self.cur.execute('select * from courses')
        return self.cur.fetchall()
    def delete(self,id):
        self.cur.execute('delete from courses where id=?',(id,))   
        self.con.commit()
    def search(self,number):
        self.cur.execute('select * from courses where pword=?',(number,))
        return self.cur.fetchall()