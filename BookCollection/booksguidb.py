from tkinter import Tk,Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox

from mysql_config import dbconfig
import mysql.connector as mcp
from booksdb import Bookdb


conn=mcp.connect(**dbconfig)


db=Bookdb()
def get_selected_row(event):
    global selected_tuple
    index=list_box.curselection()[0]
    selected_tuple=list_box.get(index)
    title_entry.delete(0,'end')
    title_entry.insert('end',selected_tuple[1])
    author_entry.delete(0,'end')
    author_entry.insert('end',selected_tuple[2])
    genre_entry.delete(0,'end')
    genre_entry.insert('end',selected_tuple[3])
    sgenre_entry.delete(0,'end')
    sgenre_entry.insert('end',selected_tuple[4])
    height_entry.delete(0,'end')
    height_entry.insert('end',selected_tuple[5])
    pub_entry.delete(0,'end')
    pub_entry.insert('end',selected_tuple[6])
    
def view_records():
    list_box.delete(0,'end')
    for row in db.view():
        list_box.insert('end',row)
        
def add_book():
    db.insert(title_text.get(),author_text.get(),genre_text.get(),sgenre_text.get(),height_text.get(),pub_text.get())
    list_box.delete(0,'end')
    list_box.insert('end',title_text.get(),author_text.get(),genre_text.get(),sgenre_text.get(),height_text.get(),pub_text.get())
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    genre_entry.delete(0,'end')
    sgenre_entry.delete(0,'end')
    height_entry.delete(0,'end')
    pub_entry.delete(0,'end')
    conn.commit()
    
def delete_book():
    db.delete(selected_tuple[0])
    conn.commit()
    
def clear_screen():
    list_box.delete(0,'end')
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    genre_entry.delete(0,'end')
    sgenre_entry.delete(0,'end')
    height_entry.delete(0,'end')
    pub_entry.delete(0,'end')
    
def update_records():
    db.update(selected_tuple[0],title_text.get(),author_text.get(),genre_text.get(),sgenre_text.get(),height_text.get(),pub_text.get())
    list_box.delete(0,'end')
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    genre_entry.delete(0,'end')
    sgenre_entry.delete(0,'end')
    height_entry.delete(0,'end')
    pub_entry.delete(0,'end')
    conn.commit()
    
def on_closing():
    dd=db
    if messagebox.askokcancel('Quit','Do you want to exit?'):
        root.destroy()
        del dd
        

root=Tk()

root.title('My Books DB')
root.configure(background='light blue')
root.geometry("1100x700")
#root.resizable(width=False,height=False)

title_label=ttk.Label(root,text='Title: ',background='blue',font=("TkDefaultFont",16))
title_label.grid(row=0,column=0,sticky=W)
title_text=StringVar()
title_entry=ttk.Entry(root,width=16,textvariable=title_text)
title_entry.grid(row=0,column=1,sticky=W)

author_label=ttk.Label(root,text='Author: ',background='blue',font=("TkDefaultFont",16))
author_label.grid(row=0,column=2,sticky=W)
author_text=StringVar()
author_entry=ttk.Entry(root,width=16,textvariable=author_text)
author_entry.grid(row=0,column=3,sticky=W)


genre_label=ttk.Label(root,text='Genre: ',background='blue',font=("TkDefaultFont",16))
genre_label.grid(row=0,column=4,sticky=W)
genre_text=StringVar()
genre_entry=ttk.Entry(root,width=16,textvariable=genre_text)
genre_entry.grid(row=0,column=5,sticky=W)

sgenre_label=ttk.Label(root,text='SUub Genre: ',background='blue',font=("TkDefaultFont",16))
sgenre_label.grid(row=1,column=0,sticky=W)
sgenre_text=StringVar()
sgenre_entry=ttk.Entry(root,width=16,textvariable=sgenre_text)
sgenre_entry.grid(row=1,column=1,sticky=W)

height_label=ttk.Label(root,text='Height: ',background='blue',font=("TkDefaultFont",16))
height_label.grid(row=1,column=2,sticky=W)
height_text=StringVar()
height_entry=ttk.Entry(root,width=16,textvariable=height_text)
height_entry.grid(row=1,column=3,sticky=W)

pub_label=ttk.Label(root,text='Publisher: ',background='blue',font=("TkDefaultFont",16))
pub_label.grid(row=1,column=4,sticky=W)
pub_text=StringVar()
pub_entry=ttk.Entry(root,width=16,textvariable=pub_text)
pub_entry.grid(row=1,column=5,sticky=W)

add_btn=Button(root,text='Add Book',bg='blue',fg='black',font='helvetica 10 bold',command=add_book)
add_btn.grid(row=1,column=6, sticky=W)

list_box=Listbox(root,height=32,width=60,font='helvetica 13',bg='light yellow')
list_box.grid(row=3,column=1,columnspan=14,sticky=W+E,pady=40,padx=15)
list_box.bind('<<ListboxSelect>>',get_selected_row)

scroll_bar=Scrollbar(root)
scroll_bar.grid(row=1,column=8,rowspan=14,sticky=W)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

view_btn=Button(root,text='View All',bg='blue',fg='black',font='helvetica 10 bold',command=view_records)
view_btn.grid(row=15,column=1)

clear_btn=Button(root,text='Clear Screen',bg='blue',fg='black',font='helvetica 10 bold',command=clear_screen)
clear_btn.grid(row=15,column=2)

exit_btn=Button(root,text='Exit Application',bg='blue',fg='black',font='helvetica 10 bold',command=on_closing)
exit_btn.grid(row=15,column=3)

modify_btn=Button(root,text='Modify Record',bg='blue',fg='black',font='helvetica 10 bold',command=update_records)
modify_btn.grid(row=15,column=4)

delete_btn=Button(root,text='Delete Record',bg='blue',fg='black',font='helvetica 10 bold',command=delete_book)
delete_btn.grid(row=15,column=5)

        
root.mainloop()