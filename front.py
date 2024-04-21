from tkinter import *
import backs

root = Tk()
root.title("books")


def get_row(event):
    global select
    if len(list_show.curselection()) > 0:
        index = list_show.curselection()[0]
        select = list_show.get(index)
        t_title.delete(0, END)
        t_title.insert(0, select[1])
        # str_title.set(select[1])
        t_isbn.delete(0, END)
        t_isbn.insert(0, select[2])
        # str_isbn.set(select[2])


def clear_list():
    list_show.delete(0, END)


def fill_list(books):
    for book in books:
        list_show.insert(END, book)


def read_com():
    clear_list()
    books = backs.read()
    fill_list(books)


def search_com():
    clear_list()
    books = backs.search(t_title.get(), t_isbn.get())
    fill_list(books)


def insert_com():
    backs.insert(title=t_title.get(), isbn=t_isbn.get())
    str_title.set("")
    str_isbn.set("")
    read_com()


def updat_com():
    backs.updat(title=t_title.get(), isbn=t_isbn.get(), id=select[0])
    read_com()


def delete_com():
    backs.delete(id=select[0])
    read_com()


str_title = StringVar()
l_title = Label(root, text="title")
l_title.grid(row=0, column=0)
t_title = Entry(root, textvariable=str_title)
t_title.grid(row=0, column=1)

str_isbn = StringVar()
l_isbn = Label(root, text="isbn")
l_isbn.grid(row=0, column=2)
t_isbn = Entry(root, textvariable=str_isbn)
t_isbn.grid(row=0, column=3)

list_show = Listbox(root, width=35, height=6)
list_show.grid(row=1, column=2, columnspan=2, rowspan=3)
sb = Scrollbar(root)
sb.grid(row=1, column=1, rowspan=2)
list_show.configure(yscrollcommand=sb)
sb.configure(command=list_show.yview)
list_show.bind("<<ListboxSelect>>", get_row)

b_show = Button(root, text="show", command=lambda: read_com())
b_show.grid(row=1, column=0)
b_search = Button(root, text="search", command=search_com)
b_search.grid(row=2, column=0)
b_updat = Button(root, text="update", command=updat_com)
b_updat.grid(row=3, column=0)
b_insert = Button(root, text="insert", command=insert_com)
b_insert.grid(row=1, column=1)
b_delet = Button(root, text="delete", command=delete_com)
b_delet.grid(row=2, column=1)
b_close = Button(root, text="close", command=root.destroy)
b_close.grid(row=3, column=1)

read_com()
root.mainloop()
