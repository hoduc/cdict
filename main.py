from tkinter import *
from tkinter.scrolledtext import *

import urllib
import urllib.request
import sys

ENTER_EVENT_ID = "<Return>"
MOUSE1_EVENT_ID = "<Button-1>"
DICT = []
STATES = ["VI_CN","CN_VI"]
LOOKUP_TYPE = STATES[0]

def lookup(event):
    print ("event:lookup:", event.widget)
    print ("looking up:", lu_input.get(), "....")
    #print(DICT[0])
    query = DICT[0][1]["sing_vi_cn"] + "=" +  urllib.parse.quote(lu_input.get().encode('utf-8'))

    with urllib.request.urlopen(query) as response:
        text.set(response.read().decode("utf-8"))
        print(text)
    
def loadDictModule(filename="config"):
    dictname=""
    dictsource={}
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == "[":
                if count:
                    DICT.append((dictname,dictsource))
                    dictsource = {}
                dictname = line[:-1]
                count += 1
            else:
                l = line.strip().split("=")
                dictsource[l[0]] = l[1]             
        DICT.append((dictname,dictsource))
        
loadDictModule()
#GUI CODE
root = Tk()
root.tk.call('encoding', 'system', 'utf-8') #make decoding available
root.geometry("300x250+300+300")
root.title("Lookup")

text = StringVar()
#displaying the result of look up
disp_frame = Frame(root)
disp_frame.pack(fill=BOTH, anchor=N, expand=True)
disp_entry = Message(disp_frame, textvariable=text)#,state=DISABLED)
disp_entry.pack(fill=BOTH, padx=10,pady=10, expand=True)

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
lu_input.focus_set()

root.mainloop()

