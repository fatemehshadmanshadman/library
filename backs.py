import sqlite3


def connect():
    con = sqlite3.connect("db_books.db")
    cursor = con.cursor()
    cursor.execute(
        "create table if not exists book(id integer primary key,title varchar,isbn varchar)"
    )
    con.commit()
    con.close()


def read():
    con = sqlite3.connect("db_books.db")
    curs = con.cursor()
    curs.execute("select * from book")
    rows = curs.fetchall()
    con.close()
    return rows


def search(title="", isbn=""):
    con = sqlite3.connect("db_books.db")
    curs = con.cursor()
    curs.execute("select * from book where title=? or isbn=?", (title, isbn))
    # con.commit()
    rows = curs.fetchall()
    con.close()
    return rows


def insert(title, isbn):
    con = sqlite3.connect("db_books.db")
    curs = con.cursor()
    curs.execute("insert into book values(null,?,?)", (title, isbn))
    con.commit()
    con.close()


def updat(id, title, isbn):
    con = sqlite3.connect("db_books.db")
    curs = con.cursor()
    curs.execute("update book set title=?,isbn=? where id=?", (title, isbn, id))
    con.commit()
    con.close()


def delete(id):
    con = sqlite3.connect("db_books.db")
    curs = con.cursor()
    curs.execute("delete from book where id=?", (id,))
    con.commit()
    con.close()


connect()
# # insert("C#", "111")
# print(search(isbn="123"))
# delete(id=3)
# print(read())
