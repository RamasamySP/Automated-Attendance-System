from importlib.util import set_loader
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_reco:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Automated Attendence System")
        
        #First Img :
        img = Image.open(r"images\white.png")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lab = Label(self.root, image=self.photoimg)
        f_lab.place(x = 0, y = 0, width = 500, height = 150)

        #Second Img :
        img1 = Image.open(r"images\white.png")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lab = Label(self.root, image=self.photoimg1)
        f_lab.place(x = 500, y = 0, width = 500, height = 150)

        #Third Img :
        img2 = Image.open(r"images\white.png")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lab = Label(self.root, image=self.photoimg2)
        f_lab.place(x = 1000, y = 0, width = 500, height = 150)


        #Background
        img3 = Image.open(r"images\grey.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x = 0, y = 150, width = 1530, height = 710)

        title_lbl = Label(bg_img, text = "Face Recognition Based Automated Attendance System", font=("times new roman",35, "bold" ), bg = "white", fg = "black")
        title_lbl.place(x = 0, y = 0, width = 1530, height = 45 )

        #Student Register button
        img4 = Image.open(r"images\student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image = self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x = 200, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Student Register", command=self.student_details,cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 200, y = 300, width = 220, height = 40)

        #Face Detection button
        img5 = Image.open(r"images\face_detection.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image = self.photoimg5, command=self.face_data,cursor="hand2")
        b1.place(x = 500, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Face Detection", command=self.face_data,cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 500, y = 300, width = 220, height = 40)

        #Attendance button
        img6 = Image.open(r"images\attendance.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image = self.photoimg6, cursor="hand2", command=self.attendace_data)
        b1.place(x = 800, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Attendance", command=self.attendace_data,cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 800, y = 300, width = 220, height = 40)

        #Help button
        img7 = Image.open(r"images\help.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image = self.photoimg7, cursor="hand2")
        b1.place(x = 1100, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Help", cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 1100, y = 300, width = 220, height = 40)

        #Train Face button
        img8 = Image.open(r"images\train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image = self.photoimg8, command=self.train_data, cursor="hand2")
        b1.place(x = 200, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Train Data", command=self.train_data, cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 200, y = 580, width = 220, height = 40)

        #Photos button
        img9 = Image.open(r"images\photoimg.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image = self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x = 500, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Photo", cursor="hand2", command=self.open_img,font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 500, y = 580, width = 220, height = 40)

        #About button
        img10 = Image.open(r"images\about.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image = self.photoimg10, cursor="hand2")
        b1.place(x = 800, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "About", cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 800, y = 580, width = 220, height = 40)

        #Logout button
        img11 = Image.open(r"images\logout.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image = self.photoimg11, cursor="hand2")
        b1.place(x = 1100, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Logout", cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 1100, y = 580, width = 220, height = 40)

    def open_img(self) :
        os.startfile("data")

    #********************** Functions buttons*********************
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendace_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)    



if __name__ == "__main__" :
    root = Tk()
    obj = Face_reco(root)
    root.mainloop()