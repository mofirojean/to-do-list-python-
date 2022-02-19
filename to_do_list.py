"""creating a to do list app GUI"""
# first we import the python module used to create GUI
from tkinter import *
from tkinter import ttk


class Todo:
    """initialising the attributes"""
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("650x410+300+150")
        """creating a label"""
        self.label = Label(self.root, text="To-Do-List", font="arial, 25 bold", width=10, bd=5, bg="steel blue", fg="white")
        self.label.pack(side="top", fill="both")

        """second label for add task"""
        self.label2 = Label(self.root, text="Add Task", font="arial, 18 bold", width=10, bd=5, bg="steel blue",
                           fg="white")
        self.label2.place(x=48, y=54)

        """third label for Tasks"""
        # will contain the list of task you want to do
        self.label3 = Label(self.root, text="Tasks", font="arial, 18 bold", width=10, bd=5, bg="steel blue",
                           fg="white")
        self.label3.place(x=320, y=54)

        """textbox that contains our task"""
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="arial, 28 italic bold")
        self.main_text.place(x=280, y=100)

        """textbox that will take in the input"""
        self.text = Text(self.root, bd=2, height=2, width=25, font="arial, 10 bold")
        self.text.place(x=20, y=128)

        """add task function"""
        def add():
            # we want to get the data from our textbox and then insert in view box
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            # storing the data in a txt file
            with open("data.txt", "a") as file:
                file.write(content)
                file.seek(0)
                file.close()
            # after the input let the text disappear
            self.text.delete(1.0, END)

        """deleting word from our task box and also from our txt file """
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open("data.txt", 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button = Button(self.root, text="Add", font="sarif, 28 bold", width=7, bd=3, bg="steel blue", fg="white", command="add")
        self.button.place(x=20, y=200)

        self.button2 = Button(self.root, text="Delete", font="sarif, 28 bold", width=7, bd=3, bg="steel blue", fg="white", command="delete")
        self.button2.place(x=20, y=300)


# create the window for the to_do_list
def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
