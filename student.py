from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql .connector
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()
    
          # first image
        img1 = Image.open("Images/scholarImages/smart-attendance.jpg")
        img1 = img1.resize((450, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=450, height=120)

        # second image
        img2 = Image.open("Images/NCIT-building.jpg")
        img2 = img2.resize((450, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=450, height=120)

        # third image
        img3 = Image.open("Images/scholarImages/Graduation-2014.jpg")
        img3 = img3.resize((450, 120), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=450, height=120)

        # background image
        img4 = Image.open("Images/face-recognition-logo.jpeg")
        img4 = img4.resize((1350, 580), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1350, height=580)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1350, height=45)  

        main_frame = Frame(bg_img, bd=7)
        main_frame.place(x=10, y=55, width=1330, height=570)
        
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font=("Calibri", 12, "bold"))
        Left_frame.place(x=10, y=10, width=650, height=500)

        img_left = Image.open("Images/scholarImages/grad2.jpg")
        img_left = img_left.resize((650, 80), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=640, height=60)
        
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                font=("Calibri", 12, "bold"), fg="green")
        current_course_frame.place(x=5, y=60, width=640, height=90)
        

        # Department
        dep_label = Label(current_course_frame, text="Department :", font=("Calibri", 10, "bold"), bg="white", fg="black")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("Calibri", 10, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "SEECS", "NBS", "S3H", "SMME","ASAB","NICE","IGIS","IESE","SADA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame,text="Course :", font=("Calibri", 10, "bold"), bg="white", fg="black")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,  font=("Calibri", 10, "bold"), state="readonly")
        course_combo["values"] = ("Select Course","OOP","DLD","Vector Calculus","TBW","Thermodynamics")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Year
        Year_label = Label(current_course_frame, text="Batch:", font=("Calibri", 10, "bold"), bg="white", fg="black")
        Year_label.grid(row=1, column=0, padx=10, sticky=W)

        Year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("Calibri", 10, "bold"), state="readonly")
        Year_combo["values"] = ("Select Year", "2019","2020", "2021", "2022", "2023")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=10, sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text="Semester :", font=("Calibri", 10, "bold"), bg="white", fg="black")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester ,font=("Calibri", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10,  sticky=W)

        
        # Student's Class Information
        
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student's Class Information",
                                          font=("Calibri", 12, "bold"), fg="green")
        student_frame.place(x=5, y=150, width=640, height=300)

        #ID
        studentID_label = Label(student_frame, text="StudentID:", font=("Calibri", 10, "bold"), bg="white",
                          fg="black")
        studentID_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(student_frame, textvariable=self.var_std_id, width=22, font=("Calibri", 10, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

        # Name
        stdName_label = Label(student_frame, text="Name:", font=("Calibri", 10, "bold"), bg="white",
                          fg="black")
        stdName_label.grid(row=0, column=2, padx=10, sticky=W)

        stdName_entry = ttk.Entry(student_frame,textvariable=self.var_std_name, width=20, font=("Calibri", 10, "bold"))
        stdName_entry.grid(row=0, column=3, padx=10,pady=10, sticky=W)

        # Section
        section_label = Label(student_frame, text="Section:", font=("Calibri", 10, "bold"), bg="white",
                          fg="black")
        section_label.grid(row=1, column=0, padx=10, sticky=W)

        section_combo = ttk.Combobox(student_frame, textvariable=self.var_div,font=("Calibri", 10, "bold"), state="readonly")
        section_combo["values"] = ("Select Section", "A","B", "C","D","E")
        section_combo.current(0)
        section_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # RollNo
        studentRoll_label = Label(student_frame, text="RollNo:", font=("Calibri", 10, "bold"), bg="white",
                          fg="black")
        studentRoll_label.grid(row=1, column=2, padx=10, sticky=W)

        studentRoll_entry = ttk.Entry(student_frame, textvariable=self.var_roll,width=20, font=("Calibri", 10, "bold"))
        studentRoll_entry.grid(row=1, column=3, padx=10,pady=10 ,sticky=W)

        # Gender
        gender_label = Label(student_frame, text="Gender:", font=("Calibri", 10, "bold"), bg="white", fg="black")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_frame, textvariable=self.var_gender,font=("Calibri", 10, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #DOB
        dob_label=Label(student_frame,text="DOB:",font=("Calibri",10,"bold"),bg="white",fg="black")
        dob_label.grid(row=3,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("Calibri",10,"bold"))
        dob_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        # Contact Number
        phone_label = Label(student_frame, text="Contact No:", font=("Calibri", 10, "bold"), bg="white",
                              fg="black")
        phone_label.grid(row=2, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(student_frame,textvariable=self.var_phone,  width=20, font=("Calibri", 10, "bold"))
        phone_entry.grid(row=2, column=3, padx=10,pady=10 ,sticky=W)

        #  Address
        address_label = Label(student_frame, text="Address:", font=("Calibri", 10, "bold"), bg="white",
                              fg="black")
        address_label.grid(row=3, column=0, padx=10, sticky=W)
        address_entry = ttk.Entry(student_frame,textvariable=self.var_address, width=22, font=("Calibri", 10, "bold"))
        address_entry.grid(row=3, column=1, padx=10,pady=10, sticky=W)

        # ==================================Radio Buttons========================================

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

         # ==================================Buttons Frame========================================
        btFrame = Frame(student_frame, relief=RIDGE, bg="white")
        btFrame.place(x=0, y=200, width=640, height=40)

        save_bt = Button(btFrame, text="Save",command=self.add_data, width=15, font=('arial', 13, 'bold'), bg="red", fg="white")
        save_bt.grid(row=0, column=0)

        update_bt = Button(btFrame, text="Update",command=self.update_data, width=15, font=('arial', 13, 'bold'), bg="red", fg="white")
        update_bt.grid(row=0, column=1)

        delete_bt = Button(btFrame, text="Delete",command=self.delete_data, width=15, font=('arial', 13, 'bold'), bg="red", fg="white")
        delete_bt.grid(row=0, column=2)

        reset_bt = Button(btFrame, text="Reset",command=self.reset_data, width=15, font=('arial', 13, 'bold'), bg="red", fg="white")
        reset_bt.grid(row=0, column=3)

        btnFrame1 = Frame(student_frame, relief=RIDGE, bg="white")
        btnFrame1.place(x=0, y=240, width=640, height=40)

        capture_photo_bt = Button(btnFrame1, text="Capture Photo Sample",command=self.generate_dataset,width=62, font=('arial', 13, 'bold'), bg="red", fg="white")
        capture_photo_bt.grid(row=1, column=0)

        
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=670, y=10, width=650, height=500)

        img_right = Image.open("Images/scholarImages/high-school-grad.jpg")
        img_right = img_right.resize((650, 80), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=640, height=60)
         # ==================================Search Systems=======================================

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Clibri",10,"bold"))
        search_frame.place(x=5,y=75,width=640,height=70)

        search_label=Label(search_frame,text="Search By:",font=("Calibri",10,"bold"),bg="Green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("Calibri",10,"bold"),state="readonly",width=11)
        search_combo["values"]=("Select","Roll","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=17,font=("Calibri",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=10,font=("tCalibri",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_bt=Button(search_frame,command=self.show_all,text="Show All",width=10,font=("Calibri",10,"bold"),bg="blue",fg="white")
        showAll_bt.grid(row=0,column=4,padx=4)
        # ==================================Table Frame==========================================
        table_frame =Frame(Right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=130,width=640,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table= ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","section","roll","gender","dob","phone","address","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("section", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

####function decleration ######
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
          try:
           
             conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")
             my_cursor=conn.cursor()
             my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_radio1.get()


                                                                                                             ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
          except Exception as es:
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def fetch_data(self):
        
          
           
             conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from student")
             data=my_cursor.fetchall()
             if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                     self.student_table.insert("",END,values=i)
              conn.commit()
             conn.close()
    def get_cursor(self,event=""):
             cursor_focus=self.student_table.focus()
             content=self.student_table.item(cursor_focus)
             data=content["values"]
             self.var_dep.set(data[0]),
             self.var_course.set(data[1]),
             self.var_year.set(data[2]),
             self.var_semester.set(data[3]),
             self.var_std_id.set(data[4]),
             self.var_std_name.set(data[5]),
             self.var_div.set(data[6]),
             self.var_roll.set(data[7]),
             self.var_gender.set(data[8]),
             self.var_dob.set(data[9]),
             self.var_phone.set(data[10]),
             self.var_address.set(data[11]),
             self.var_radio1.set(data[12])

 

#============= Update function =========================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        else:
            try:
               
                Upadate = messagebox.askyesno("Upadate","Do You Want To Update This Student Details",parent=self.root)
                if Upadate>0:
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))   
                
                
                else:
                    if not Upadate:
                        return
             
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
               
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

# ===================Delete Function===================
    def delete_data(self):
        if self.var_std_id.get()=="":
           
            messagebox.showerror("Error","Student Id Must be Required",parent=self.root)
        else:
            try:
              
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")

                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
             
                messagebox.showinfo("Delete","Student Details Successfully deleted",parent=self.root)

            except Exception as es:
               
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")

                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                    ))   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ..................load predefined data  face forntal from opencv.............
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)

                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/"+"user"+"."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

            
                messagebox.showinfo("Result","Generation of data set completed!!!",parent=self.root)
            except Exception as es:
                
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")
              
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                       
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
              
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

            # show all 
    def show_all(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="igisbliss43*",database="face_recognizer")
      
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


           

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
