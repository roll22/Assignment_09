from tkinter import *
from tkinter import messagebox

class StudentGUI:
    """
      Implement the graphic user interface for add/list students
    """
    def __init__(self, ctrl):
        self.ctrl = ctrl

    def startUI(self):
        self.tk = Tk()
        self.tk.title("Student CRUD")

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        lbl = Label(frame, text="ID:")
        lbl.pack(side=LEFT)

        self.idtf = Entry(frame, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(frame, text="Name:")
        lbl.pack(side=LEFT)

        self.nametf = Entry(frame, {})
        self.nametf.pack(side=LEFT)

        lbl = Label(frame, text="Street:")
        lbl.pack(side=LEFT)

        self.streettf = Entry(frame, {})
        self.streettf.pack(side=LEFT)

        lbl = Label(frame, text="Nr.:")
        lbl.pack(side=LEFT)

        self.nrtf = Entry(frame, {})
        self.nrtf.pack(side=LEFT)

        lbl = Label(frame, text="City:")
        lbl.pack(side=LEFT)

        self.citytf = Entry(frame, {})
        self.citytf.pack(side=LEFT)

        self.storeBtn = Button(frame, text="Store", command=self.__storePressed)
        self.storeBtn.pack(side=LEFT)

        self.listBtn = Button(frame, text="List", command=self.__listStudents)
        self.listBtn.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.tk.mainloop()

    def __storePressed(self):
        """
          Handler method for store button pressed
          Store the student
          Show error messages on exceptions
        """
        try:
            st = self.ctrl.create(self.idtf.get(), self.nametf.get(), self.streettf.get(), self.nrtf.get(), self.citytf.get())
            messagebox.showinfo("Stored", "Student %s saved.." % st.getName())
            print
        except Exception as e:
            messagebox.showinfo("Error", "Error saving student - " + str(e))

    def __listStudents(self):
        """
          Handler method for list button
          Show all the students
        """
        sts = self.ctrl.search("")
        txt = "ID".ljust(5) + "Name".ljust(15) + "Address\n"
        for st in sts:
            txt += st.getId().ljust(5) + st.getName().ljust(15) + str(st.getAdr())
            txt += "\n"
        messagebox.showinfo("List students", txt)
