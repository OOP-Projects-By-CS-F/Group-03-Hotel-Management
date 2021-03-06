from tkinter import *
from tkinter.ttk import Combobox
def Description():
    window=Tk()
    window.geometry("460x900")
    window.configure(bg="#add8e6")
    window.title("Waterfall Room Description")
    l1=Label(window, text="1. Single:-", font="Times 10 bold underline", bg="#aed006")
    l2=Label(window, text="The room comes with a single bed and has sufficient space along \nwith attached bathroom and private almirah for one person",font=(6), bg="#add8e6")
    l3=Label(window, text="Costing:-\t2000/night", font=(2), bg="#add8e6")
    l4=Label(window, text="Rooms Numbers:-\t1-9", font=(2), bg="#add8e6")
    l1.grid(row=0, column=0, sticky=W)
    l2.grid(row=1, column=0, sticky=W)
    l3.grid(row=2, column=0, sticky=W)
    l4.grid(row=3, column=0, sticky=W)
    l5=Label(window, text="2. Double:-", font="Times 10 bold underline", bg="#aed006")
    l6=Label(window, text="The room comes with two single beds and has sufficient space \nalong with attached bathroom and private almirah for two person",font=(2), bg="#add8e6")
    l7=Label(window, text="Costing:-\t3000/night", font=(2), bg="#add8e6")
    l8=Label(window, text="Rooms Numbers:-\t10-19", font=(2), bg="#add8e6")
    l5.grid(row=5, column=0, sticky=W)
    l6.grid(row=6, column=0, sticky=W)
    l7.grid(row=7, column=0, sticky=W)
    l8.grid(row=8, column=0, sticky=W)
    l9=Label(window, text="3. Triple:-", font="Times 10 bold underline", bg="#aed006")
    l10=Label(window, text="The room comes with three single beds and has sufficient space \nalong with attached bathroom and private almirah for three person",font=(2), bg="#add8e6")
    l11=Label(window, text="Costing:-\t3500/night", font=(2), bg="#add8e6")
    l12=Label(window, text="Rooms Numbers:-\t20-30", font=(2), bg="#add8e6")
    l9.grid(row=9, column=0, sticky=W)
    l10.grid(row=10, column=0, sticky=W)
    l11.grid(row=11, column=0, sticky=W)
    l12.grid(row=12, column=0, sticky=W)
    l13=Label(window, text="4. Queen:-", font="Times 10 bold underline", bg="#aed006")
    l14=Label(window, text="The room comes with a queen size bed and has \na work table with attached bathroom and shared almirah for \ntwo person",font=(2), bg="#add8e6")
    l15=Label(window, text="Costing:-\t4000/night", font=(2), bg="#add8e6")
    l16=Label(window, text="Rooms Numbers:-\t31-40", font=(2), bg="#add8e6")
    l13.grid(row=13, column=0, sticky=W)
    l14.grid(row=14, column=0, sticky=W)
    l15.grid(row=15, column=0, sticky=W)
    l16.grid(row=16, column=0, sticky=W)
    l17=Label(window, text="5. Suite:-", font="Times 10 bold underline", bg="#aed006")
    l18=Label(window, text="The room comes with two rooms and has a work table, two double\n beds and a child bed with attached bathroom and shared \nalmirah for two person in every room",font=(2), bg="#add8e6")
    l19=Label(window, text="Costing:-\t5000/night", font=(2), bg="#add8e6")
    l20=Label(window, text="Rooms Numbers:-\t41-45", font=(2), bg="#add8e6")
    l17.grid(row=17, column=0, sticky=W)
    l18.grid(row=18, column=0, sticky=W)
    l19.grid(row=19, column=0, sticky=W)
    l20.grid(row=20, column=0, sticky=W)
    l21=Label(window, text="6. President Suite:-", font="Times 10 bold underline", bg="#aed006")
    l22=Label(window, text="The room comes with three bed rooms, a kitchen and a \nsitting space and has three work tables, three double beds and a \nchild room with attached bathrooms and shared almirah for two \nperson in every room. It also comes with a complementary \nbreakfast, lunch and dinner",font=(2), bg="#add8e6")
    l24=Label(window, text="Rooms Numbers:-\t46-48", font=(2), bg="#add8e6")
    l23=Label(window, text="Costing:-\t9000/night", font=(2), bg="#add8e6")
    l21.grid(row=21, column=0, sticky=W)
    l22.grid(row=22, column=0, sticky=W)
    l23.grid(row=23, column=0, sticky=W)
    l24.grid(row=24, column=0, sticky=W)
    window.mainloop()

