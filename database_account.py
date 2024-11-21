import sqlite3
def create():
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tableAccount(id INTEGER PRIMARY KEY,firstname TEXT, lastname TEXT, username TEXT, password TEXT, country TEXT, state TEXT, date TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount")
    rows = cur.fetchall()
    con.close()
    return rows

def search(firstname="", lastname="", username="", password="", country="", state="", date=""):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount WHERE firstname=? or lastname=? OR username=? OR password=? OR country=? OR state=? OR date=?", (firstname, lastname, username, password, country, state, date))
    rows = cur.fetchall()
    con.close()
    return rows
def add(firstname,lastname, username, password, country, state, date):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tableAccount VALUES(NULL,?,?,?,?,?,?,?)", (firstname, lastname, username, password, country, state, date))
    con.commit()
    con.close()
def update(firstname, lastname, username, password, country, state, date):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("UPDATE tableAccount SET firstname=?,lastname=?, username=?, password=?, country=?, state=?, date=? WHERE ", (firstname, lastname, username, password, country, state, date))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tableAccount WHERE id=?",(id,))
    con.commit()
    con.close()
create()

