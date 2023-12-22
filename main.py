from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from tkinter import messagebox
from attendance import Attendance
from face_recognition import Face_Recognition
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       #image
        img1 = Image.open("Images/nust2.jpg")
        img1 = img1.resize((1530, 120))

        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1530, height=120)

        img2 = Image.open("Images/ai-shutterstock.jpg")
        img2 = img2.resize((1530, 400))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=120, width=1530, height=625)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("Times New Roman", 35, "bold"), bg="white", fg="Black")
        title_lbl.place(x=0, y=0, width=1530, height=45)  

        # different buttons with images
        # student button
        img3 = Image.open("Images/student.jpg")
        img3 = img3.resize((195, 195))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bt1 = Button(bg_img ,command=self.student_details,image=self.photoimg3, cursor="hand2")
        bt1.place(x=175, y=80, width=195, height=195)

        bt1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        bt1_1.place(x=175, y=245, width=195, height=40)

        # Face Detection button
        img4 = Image.open("Images/faceDetector.jpeg")
        img4 = img4.resize((195, 195))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bt2 = Button(bg_img,command=self.face_data, image=self.photoimg4, cursor="hand2")
        bt2.place(x=560, y=80, width=195, height=195)

        bt2_2 = Button(bg_img, text="Face Detector",command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        bt2_2.place(x=560, y=245, width=195, height=40)

        # attendance button
        img5 = Image.open("Images/face.jpg")
        img5 = img5.resize((195, 195))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        bt3 = Button(bg_img, command=self.attendance_data,image=self.photoimg5, cursor="hand2")
        bt3.place(x=1000, y=80, width=195, height=195)

        bt3_3 = Button(bg_img, text="Attendance",command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        bt3_3.place(x=1000, y=245, width=195, height=40)


        # train data button
        img6 = Image.open("Images/trainFace-khom.png")
        img6 = img6.resize((195, 195))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        bt4 = Button(bg_img, image=self.photoimg6, command=self.train_data,cursor="hand2")
        bt4.place(x=175, y=350, width=195, height=195)

        bt4_4 = Button(bg_img, text="Train Data",command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        bt4_4.place(x=175, y=525, width=195, height=40)

        # Photos button
        img7 = Image.open("Images/photos.jpg")
        img7 = img7.resize((195, 195))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        bt5 = Button(bg_img,command=self.open_image, image=self.photoimg7,cursor="hand2")
        bt5.place(x=560, y=350, width=195, height=195)

        bt5_5 = Button(bg_img, text="Photos", command=self.open_image,cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        bt5_5.place(x=560, y=525, width=195, height=40)

        # Exit button
        img8 = Image.open("Images/exit-sign-neon-style_77399-144.jpg")
        img8 = img8.resize((195,195))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        bt6 = Button(bg_img, command=self.iexit,image=self.photoimg8, cursor="hand2")
        bt6.place(x=1000, y=350, width=195, height=195)

        bt6_6 = Button(bg_img, text="Exit",command=self.iexit, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        bt6_6.place(x=1000, y=525, width=195, height=40)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    def open_image(self):
        os.startfile("data")
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def iexit(self):
        self.iexit=messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
if __name__ == "__main__":
    root = Tk()

    obj = Face_Recognition_System(root)
    root.mainloop()
