import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import time


root = Tk()
root.title("Admin Page")
height = root.winfo_screenheight()-100
width = (root.winfo_screenwidth())//2
widget_width = width//2
root.geometry("{}x{}".format(width, height))
root.resizable(0,0)



class admin:
    def main():

        label_search = Label(root, text='Search Matric Num', font=('helvetical', 13))
        label_search.place(x = 310, y = 33)

        global entry_search
        entry_search = Entry(root)
        entry_search.place(x = 460, y = 30, width=widget_width-150, height=height//26)

        btn_search = Button(root, text="Search", background=('blue'), font=('helvetical', 8, 'bold'), fg=('white'), command=lambda:search())
        btn_search.place(x = 698, y = 30, width=width-700, height=height//26)

        global label_result
        label_result = ttk.Treeview(root, style="mystyle.Treeview")
        label_result['columns']= ("Name", "Matric ID", "Time-In","Course", "Session", "Date")
        label_result.column("#0", width=-30, stretch=NO)
        label_result.column("Name", width=110)
        label_result.column("Matric ID", width=90, anchor = CENTER)
        label_result.column("Time-In", width=35, anchor = CENTER)
        label_result.column("Course", width=80, anchor = CENTER)
        label_result.column("Session", width=40, anchor = CENTER)
        label_result.column("Date", width=90, anchor = CENTER)
        label_result.place(x = 20, y= 80, width= width-50,  height = 600)
        label_result.heading("Name", text = "Name")
        label_result.heading("Matric ID", text = "Matric ID")
        label_result.heading("Time-In", text = "Time-In")
        label_result.heading("Course", text = "Course")
        label_result.heading("Session", text = "Session")
        label_result.heading("Date", text = "Date")

        style =ttk.Style()
        font1 = ['Times',12, 'normal']
        font2 = ['Times',10, 'normal']
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=font2)
        style.configure("mystyle.Treeview.Heading",font=font1)
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        label_course = Label(root, text='Choose Course To View/Search', font=('helvetical', 10))
        label_course.place(x = 20, y = 690)

        global course_drop
        clicked = StringVar()
        options = ['Embedded System', 'Python Language', 'Web Design']
        course_drop = ttk.Combobox (root, values = options,font=('san-serif', 10), textvariable = clicked)
        course_drop.place(x =20, y = 715, width = width/3, height = height//20)
    
        btn_view = Button(root, text="View Records", background=('red'), font=('helvetical', 13, 'bold'), fg=('white'), command=lambda:backend())
        btn_view.place(x = 350, y = 715, width=width/2, height=height//20)


        def backend():
            course = course_drop.get()


            for item in label_result.get_children():
                label_result.delete(item)

            if course == "":
                messagebox.showerror("Error", "Please Pick A Course To View From")
            else:
                try:
                    mydb = mysql.connector.connect(
                        host = "sql8.freemysqlhosting.net",
                        user= "sql8675279",
                        password = "3JQ694I3DZ",
                        port= 3306,
                        database="sql8675279"
                        )
                    cursor = mydb.cursor()

                    if course == "Embedded System":
                        view_att = """ SELECT * FROM embed"""
                        cursor.execute(view_att)
                        results = cursor.fetchall()
                        if results == "":
                            messagebox.showerror("Error","Empty Record")
                        else:
                            for i in results:
                                label_result.insert("",'end', values=(i[0], i[21], i[1], i[20], i[5], (i[7], i[6])))

                    elif course == "Python Language":
                        view_att = """ SELECT * FROM python"""
                        cursor.execute(view_att)
                        results = cursor.fetchall()
                        if results == "":
                            messagebox.showerror("Error","Empty Record")
                        else:
                            for i in results:
                                label_result.insert("",'end', values=(i[1], i[2], i[3], i[4], i[5], i[6]))
                    elif course == "Web Design":
                        view_att = """ SELECT * FROM web"""
                        cursor.execute(view_att)
                        results = cursor.fetchall()
                        if results == "":
                            messagebox.showerror("Error","Empty Record")
                        else:
                            for i in results:
                                label_result.insert("",'end', values=(i[1], i[2], i[3], i[4], i[5], i[6]))
                    else:
                        messagebox.showerror("Error", "Invalid")
                
                except Exception:
                    messagebox.showerror("Connection Error","Internet Connection is Required")

        def search():
            course = course_drop.get()

            for item in label_result.get_children():
                label_result.delete(item)

            list1 = []
            search = entry_search.get()
            list1.append(search)

            if course == "":
                messagebox.showerror("Error", "Please Pick A Course To Search From")
            else:
                try:
                    mydb = mysql.connector.connect(
                        host = "sql8.freemysqlhosting.net",
                        user= "sql8675279",
                        password = "3JQ694I3DZ",
                        port= 3306,
                        database="sql8675279"
                        )
                    cursor = mydb.cursor()


                    search_att = """ SELECT * FROM %s where Matric_Num = %s"""
                    vals = (course, list1)
                    cursor.execute(search_att, vals)
                    results = cursor.fetchall()

                    for i in results:
                        label_result.insert("",'end', values=(i[1], i[2],i[3], i[4], i[5], i[6]))


                except Exception:
                    messagebox.showerror("Connection Error","Internet Connection is Required")





    main()
if __name__ == '__main__':
    admin()
    root.mainloop()