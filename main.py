from Tkinter import *

root = Tk()
root.geometry("250x150+300+300")
app = Frame(root)
app.parent = root
app.parent.title("Lookup")
app.pack(fill=BOTH, expand=1)

disp_frame = Frame(app)
disp_frame.pack(fill=BOTH, anchor=N, expand=True)
disp_entry = Entry(disp_frame, state='disabled')
disp_entry.pack(fill=BOTH, padx=5,pady=5, expand=True)

lu_frame = Frame(app)
lu_frame.pack(fill=X, anchor=S )
lu_label = Label(lu_frame, text="Enter:")
lu_label.pack(side=LEFT, padx=5, pady=5)
lu_input = Entry(lu_frame)
lu_input.pack(fill=X, padx=5, pady=5)

root.mainloop()

