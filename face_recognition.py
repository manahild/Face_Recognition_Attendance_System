import cv2
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import mysql.connector
import pyttsx3
from student import Student
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.attendance_marked_set = set()
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Algerian", 20, "bold"), bg="lightblue",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=35)

        img_bottom = Image.open(r"Images\re1.jpg")
        img_bottom = img_bottom.resize((1366, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=50, width=1366, height=650)

        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog,
                      font=("times new roman", 15, "bold"), bg="darkgreen", fg="yellow")
        b1_1.place(x=500, y=450, width=300, height=150)

    def mark_attendance(self, i, r, n, d):
     student_key = (i, r, n, d)
     if student_key not in self.attendance_marked_set:
       with open("attendance.csv", "a+") as f:
        my_data_list = f.readlines()
        name_list = [entry.split(",")[0] for entry in my_data_list]

        if i not in name_list and r not in name_list and n not in name_list and i not in name_list:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")

            # Update this line to concatenate values with commas
            entry = f"{i[0]},{r[0]},{n[0]},{d[0]},{dtString},{d1},Present\n"
            f.write(entry)
       self.attendance_marked_set.add(student_key)
       return True  # Attendance marked successfully
     return False 

    def face_recog(self):
        def draw_boundary(img, classifier, scale_factor, min_neighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scale_factor, min_neighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w + 20, y + h + 20), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h + 20, x:x + w + 20])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="igisbliss43*",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_id=" + str(id))

                n = my_cursor.fetchone()
                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                my_cursor.execute("select  Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()

                if confidence > 77:
                    self.mark_attendance(i, r, n, d)
                    text_lines = [
                        f"Student_id: {i[0]}",
                        f"Roll: {r[0]}",
                        f"Name: {n[0]}",
                        f"Department: {d[0]}"
                    ]
                  

                    for z, line in enumerate(text_lines):
                        cv2.putText(img, line, (x, y - 75 + z * 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    break
                else:
                    cv2.rectangle(img, (x, y), (x + w + 20, y + h + 20), (0, 0, 255), 3)
                    engine.say("Warning!!! Unknown Face")
                    engine.runAndWait()
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, face_cascade):
            coord = draw_boundary(img, face_cascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face_cascade)

            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()




