from Tkinter import *

ENTER_EVENT_ID = "<Return>"
MOUSE1_EVENT_ID = "<Button-1>"

def lookup(event):
    print "event:lookup:", event.widget
    print "looking up:", lu_input.get(), "...."
    
root = Tk()
root.geometry("250x150+300+300")
root.title("Lookup")

#displaying the result of look up
disp_frame = Frame(root)
disp_frame.pack(fill=BOTH, anchor=N, expand=True)
disp_entry = Entry(disp_frame, state=DISABLED)
disp_entry.pack(fill=BOTH, padx=5,pady=5, expand=True)

#input to the lookup
lu_frame = Frame(root, name="lookup_frame")
lu_frame.pack(fill=X, anchor=S )
lu_label = Label(lu_frame, text="Enter:")
lu_label.pack(side=LEFT, padx=5, pady=5)
lu_button = Button(lu_frame, text="Look up!!!", name="lookup_button")
lu_button.pack(side=RIGHT, padx=5, pady=5)
lu_button.bind(MOUSE1_EVENT_ID, lookup)
lu_input = Entry(lu_frame, name="lookup_input")
lu_input.pack(fill=X, padx=5, pady=5)
lu_input.bind(ENTER_EVENT_ID, lookup)

root.mainloop()

