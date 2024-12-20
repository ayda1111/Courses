from tkinter import *
from tkinter import messagebox
from backend import Database
root=Tk()
root.geometry('500x500')
root.title('ثبت نام دوره ها')
root.config(bg='light grey')
db=Database('f:/python/term3/registering/mydb.db')
#Functions========================
def show():
    lst_info.delete(0,END)
    res=db.fetch()
    for i in res:
        lst_info.insert(END,f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}')
def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_course.delete(0,END)
    ent_pword1.delete(0,END)
    ent_name.focus_set()
def add_item():
    if not ent_name.get() or not ent_lname.get() or not ent_pword1.get():
        messagebox.showerror('نادرست','اطلاعات ضروری را کامل کنید')
        return
    d1=db.search(ent_pword1.get())
    if d1:
        messagebox.showerror('رمز تکراری','رمز نامعتبر است . لطفا رمز دیگری وارد کنید')
    db.add(ent_name.get(),ent_lname.get(),ent_course.get(),ent_pword1.get())
    show()
    clear()
def delete_item():
    index=lst_info.curselection()
    data=lst_info.get(index)
    finaldata=data.split(',')
    ask=messagebox.askyesno('حذف کردن','آیا از پاک کردن اطمینان دارید؟')
    if ask==True:
        db.delete(finaldata[0])
    show()
    clear()
def enter():
    d=db.search(ent_pword2.get())
    print(db.search(ent_pword2.get()))
    if not db.search(ent_pword2.get()):
        messagebox.showerror('بدون حساب کاربری','شما هنوز در سیستم ثبت نام نکرده اید')
        return
    root.destroy()
    win=Tk()
    win.geometry('300x300')
    win.title('ورود با موفقیت')
    win.config(bg='blue')
    for i in d:
        lbl_welcome=Label(win,text=f' !خوش آمدید ،{i[1]} {i[2]}',bg='light blue',fg='black',font='BNazanin 12 bold')
        lbl_welcome.place(x=50,y=120)
    win.mainloop()
def select(event):
    index=lst_info.curselection()
    data=lst_info.get(index)
    finaldata=data.split(',')
    clear()
    ent_name.insert(0,finaldata[1])
    ent_lname.insert(0,finaldata[2])
    ent_course.insert(0,finaldata[3])
    ent_pword1.insert(0,finaldata[4])

#Labels===========================
lbl_name=Label(text=':نام ',bg='light grey',fg='black',font='BNazanin 12 bold')
lbl_name.place(x=425,y=30)
lbl_lname=Label(text=' :نام خانوادگی ',bg='light grey',fg='black',font='BNazanin 12 bold')
lbl_lname.place(x=150,y=30)
lbl_course=Label(text=':نام دوره ',bg='light grey',fg='black',font='BNazanin 12 bold')
lbl_course.place(x=425,y=80)
lbl_pword1=Label(text=':رمز ورود',bg='light grey',fg='black',font='BNazanin 12 bold')
lbl_pword1.place(x=150,y=80)
lbl_pword2=Label(text=':رمز ورود',bg='light grey',fg='black',font='BNazanin 12 bold')
lbl_pword2.place(x=365,y=450)
lbl_nec1=Label(text='*',bg='light grey',fg='red',font='BNazanin 12 bold')
lbl_nec1.place(x=455,y=30)
lbl_nec2=Label(text='*',bg='light grey',fg='red',font='BNazanin 12 bold')
lbl_nec2.place(x=235,y=30)
lbl_nec3=Label(text='*',bg='light grey',fg='red',font='BNazanin 12 bold')
lbl_nec3.place(x=230,y=80)
#Buttons==========================
btn_show=Button(text='مشاهده همه',bg='dark grey',activebackground='white',fg='black',width=15,font='BNazanin 11 bold',pady=9,command=show)
btn_show.place(x=340,y=130)
btn_add=Button(text='اضافه کردن',bg='dark grey',activebackground='white',fg='black',width=15,font='BNazanin 11 bold',pady=9,command=add_item)
btn_add.place(x=340,y=180)
btn_delete_entries=Button(text='خالی کردن ورودی ها',bg='dark grey',activebackground='white',fg='black',width=15,font='BNazanin 11 bold',pady=9,command=clear)
btn_delete_entries.place(x=340,y=230)
btn_delete=Button(text='حذف کردن',bg='dark grey',activebackground='white',fg='black',width=15,font='BNazanin 11 bold',pady=9,command=delete_item)
btn_delete.place(x=340,y=280)
btn_close=Button(text='خروج',bg='dark grey',activebackground='white',fg='black',width=15,font='BNazanin 11 bold',pady=9)
btn_close.place(x=340,y=330)
btn_enter=Button(text='ورود به سامانه',bg='dark grey',activebackground='white',fg='black',width=15,font='BNazanin 11 bold',pady=9,command=enter)
btn_enter.place(x=340,y=380)
#Entries============================
ent_name=Entry(width=20)
ent_name.place(x=300,y=32)
ent_lname=Entry(width=20)
ent_lname.place(x=25,y=33)
ent_course=Entry(width=20)
ent_course.place(x=300,y=80)
ent_pword1=Entry(width=20)
ent_pword1.place(x=20,y=80)
ent_pword2=Entry(width=50)
ent_pword2.place(x=60,y=453)
#Listbox
lst_info=Listbox(bg='dark grey',width=40,height=19)
lst_info.place(x=20,y=130)

lst_info.bind('<<ListboxSelect>>',select)

root.mainloop()