import tkinter as tk
from tkinter import messagebox
from file_connection import *
zagr=get_articles()
q=None
def show_articles():
    global q
    index=listbox.curselection()
    if index:
        nazv=listbox.get(index)
        nazv2=nazv
        text.delete(1.0, tk.END)
        text.insert(tk.END, zagr[nazv2])
        title_label.config(text=nazv)
        title_label.pack()
        text.pack()
        butt.pack()
        butt_del.pack_forget()
        butt_show.pack_forget()
        butt_add.pack_forget()
        listbox.pack_forget()


def nazad():
    global q
    q=None
    text.delete(1.0, tk.END)
    title_label.config(text='')
    listbox.pack(fill=tk.BOTH)
    text.pack_forget()
    title_label.pack_forget()
    butt.pack_forget()
    butt_show.pack()
    butt_del.pack()
    butt_add.pack()

def del_articles():
    global q, zagr, listbox
    index = listbox.curselection()
    if index:
        article=listbox.get(index)
        article2 = article
        ask=messagebox.askyesno('удаление','вы действительно хотите удалить файл?')
        if ask:
            nazad()
            del zagr[article]
            listbox.delete(index)
            delete_article(article)

def add_article():
    global listbox, article, zagr
    window=tk.Toplevel(root)
    window.title('добавить статью')
    label=tk.Label(window, text="введите название вашей статьи: ")
    label.pack()
    entry=tk.Entry(window)
    entry.pack()
    text=tk.Label(window, text= 'введите текст статьи: ')
    text.pack()
    text2=tk.Text(window, wrap=tk.WORD)
    text2.pack()
    def safe():
        entry2=entry.get()
        text3=text2.get('1.0', tk.END)
        if entry2 and text3:
            zagr[entry2]=text3
            listbox.insert(0, entry2)
            zapis(entry2, text3)
            window.destroy()
            show_articles()
    butt_save = tk.Button(window, text='cохранить', command=safe)
    butt_save.pack()


root=tk.Tk()
root.title('Сборники')
root.geometry('700x400')
listbox=tk.Listbox(root)
listbox.pack(fill=tk.BOTH)
for i in zagr:
    listbox.insert(tk.END, i)
text = tk.Text(root, wrap=tk.WORD)
text.pack()
text.pack_forget()
title_label=tk.Label(root, text='' )
title_label.pack() #можно добавить шрифты
title_label.pack_forget()
butt=tk.Button(root, text='назад', command=nazad)
butt.pack()
butt.pack_forget()
butt_show=tk.Button(root, text='открыть', command=show_articles)
butt_show.pack()

butt_add=tk.Button(root, text='добавить', command=add_article)
butt_add.pack()

butt_del=tk.Button(root, text='удалить', command=del_articles)
butt_del.pack()


root.mainloop()
