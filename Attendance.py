import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import time
import mysql.connector



root = Tk()
root.title("CodeVerse")
height = root.winfo_screenheight()//2
width = (root.winfo_screenwidth())//4
root.geometry("{}x{}".format(width, height))
root.resizable(0,0)
height_widget = root.winfo_screenheight()//20

class attendance:
    def main():
        #Widget design section
        label_name = Label(root, text='Name', font=('helvetical', 13))
        label_name.place(x = 20, y = 10)

        global entry_name
        entry_name = Entry(root, font=('times-new-roman', 13))
        entry_name.place(x = 20, y = 40, width=width-50, height=height_widget)

        label_matric = Label(root, text='Matric Number', font=('helvetical', 13))
        label_matric.place(x = 20, y = 95)

        global entry_matric
        entry_matric = Entry(root,font=('san-serif', 13))
        entry_matric.place(x = 20, y = 120, width=width-50, height=height_widget)

        label_course = Label(root, text='Course', font=('helvetical', 13))
        label_course.place(x = 20, y = 170)

        global course_drop
        clicked = StringVar()
        options = ['Embedded System', 'Python Language', 'Web Design']
        course_drop = ttk.Combobox (root, values = options,font=('san-serif', 13), textvariable = clicked)
        course_drop.place(x =20, y = 200, width = width-50, height = height_widget)

        label_session = Label(root, text='Session', font=('helvetical', 13))
        label_session.place(x = 20, y = 250)

        global session_drop
        clicked = StringVar()
        options = ['Morning', 'Afternoon', 'Double']
        session_drop = ttk.Combobox (root, values = options,font=('san-serif', 13), textvariable = clicked)
        session_drop.place(x =20, y = 280, width = width-230, height = height_widget)
       
        btn_submit = Button(root, text='Submit', background='blue', foreground='white', font=(2), command=lambda:data_process())
        btn_submit.place(x = 200, y = 280, width= width-230, height=height_widget)


        def data_process():
            name = entry_name.get().upper()
            matric = entry_matric.get()
            session = session_drop.get()
            course = course_drop.get()
           


            if session == "" or matric == "" or name == "" or course == "":
                messagebox.showerror("Error", "Invalid/Empty Entry")
            else:
                asking = messagebox.askyesno('CONFIRMATION', 'Check for incorrect details... Do You want to Continue to Submission?')
                if asking:
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")

                    
                    try:
                        timestamp = time.time()
                        current_date = time.ctime(timestamp)
                        day = current_date[0:4] 
                        print(day)
                      

                        mydb = mysql.connector.connect(
                            host = "sql8.freemysqlhosting.net",
                            user= "sql8675279",
                            password = "3JQ694I3DZ",
                            port= 3306,
                            database="sql8675279"
                            )
                        cursor = mydb.cursor()

                        if course == 'Embedded System':
                            embed_table = """CREATE TABLE if not exists embed (
                                        id INT AUTO_INCREMENT PRIMARY KEY,
                                        Name VARCHAR(50),
                                        Matric_Num VARCHAR(20),
                                        Time_In VARCHAR(12) NOT NULL,
                                        Course VARCHAR(20) NOT NULL,
                                        Session VARCHAR(50),
                                        Date VARCHAR(11) NOT NULL,
                                        Day VARCHAR(5)
                                        )"""
                            cursor.execute(embed_table)
                            mydb.commit()
                            insert_table = """INSERT INTO embed (
                                            Name, Matric_Num,Time_In,Course, Session, Date,Day)
                                            VALUES(%s,%s,%s,%s,%s,now(),%s)"""
                            vals = (name, matric,current_time,course, session, day)
                            cursor.execute(insert_table, vals)
                            mydb.commit()
                            messagebox.showinfo("Successful", "Attndance Taken")
                        elif course == 'Python Language':
                            py_table = """CREATE TABLE if not exists python (
                                        id INT AUTO_INCREMENT PRIMARY KEY,
                                        Name VARCHAR(50),
                                        Matric_Num VARCHAR(20),
                                        Time_In VARCHAR(12) NOT NULL,
                                        Course VARCHAR(20) NOT NULL,
                                        Session VARCHAR(50),
                                        Date VARCHAR(11) NOT NULL,
                                        Day VARCHAR(5)
                                        )"""
                            cursor.execute(py_table)
                            mydb.commit()
                            print("Worked to this point")
                            insert_table = """INSERT INTO python(
                                            Name, Matric_Num,Time_In,Course, Session, Date, Day)
                                            VALUES(%s,%s,%s,%s,%s,now(), %s)"""
                            vals = (name, matric,current_time,course, session, day)
                            cursor.execute(insert_table, vals)
                            mydb.commit()
                            messagebox.showinfo("Successful", "Attndance Taken")
                        elif course == 'Web Design':
                            web_table = """CREATE TABLE if not exists web (
                                        id INT AUTO_INCREMENT PRIMARY KEY,
                                        Name VARCHAR(50),
                                        Matric_Num VARCHAR(20),
                                        Time_In VARCHAR(12) NOT NULL,
                                        Course VARCHAR(20) NOT NULL,
                                        Session VARCHAR(50),
                                        Date VARCHAR(11) NOT NULL,
                                        Day VARCHAR(5)
                                        )"""
                            cursor.execute(web_table)
                            mydb.commit()
                            insert_table = """INSERT INTO web(
                                            Name, Matric_Num,Time_In,Course, Session, Date)
                                            VALUES(%s,%s,%s,%s,%s,now(),%s)"""
                            vals = (name, matric,current_time,course, session, day)
                            cursor.execute(insert_table, vals)
                            mydb.commit()
                            messagebox.showinfo("Successful", "Attndance Taken")
                        
                        else:
                            messagebox.showerror("Error","Invalid Input at Choosing Course ")

                        mydb.close()

                    except Exception:
                        messagebox.showerror("Connection Error","Internet Connection is Required")
                        # entry_matric.delete('item')

                else:
                    pass
    main()
if __name__ == '__main__':
    attendance()
    root.mainloop()