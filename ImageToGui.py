from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
currdir = os.getcwd()
tempdir = ''
width = 750;

global w1
global w2
global w3
global w4
global entry
var = None

delay = 500
global label
global frame2
global frame_31
global frame_32
global blank2

def browse():
    currdir = os.getcwd()
    global tempdir
    tempdir = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("png", "*.png")))

def refresh_gui():
	pass


def twitch():
    global width
    width = "twitch"
    entry.delete(0,END)
    entry.insert(0,34)
def youtube():
    global width
    width = "youtube"
    entry.delete(0,END)
    entry.insert(0,56)

def start():
    from ImageToAscii import handle_image_conversion
    from ImageToAscii import get_enhance_image;global w1;global w2;global w3;global w4
    print (w1.get());
    width = entry.get()
    try:
        var = int(width)
        if var<10 or var>750 :
            root.after(delay, start)
    except:
        root.after(delay, start)
    handle_image_conversion(tempdir, width, w1.get(), w2.get(), w3.get(), w4.get());
    photo = ImageTk.PhotoImage(get_enhance_image());
 



    global blank2
    global frame_31
    global frame_32
    global label
    global label2
    blank2.destroy()
    frame_31.destroy()
    frame_32.destroy()
    label.destroy()
    label2.destroy()
    blank2 = Frame(root)
    Grid.columnconfigure(blank2, 2, weight = 1)

    
    frame_31 = Frame(blank2)
    label = Label(frame_31, image = photo )
    label.image = photo
    label.text = ""
    
    label.pack(side = LEFT)
    #print(label)
    #global label

    

    frame_32 = Frame(blank2)
    with open("temp.txt") as f:
        linewidth = len(f.readline())
        label = Label(frame_32, text=f.read())
        if linewidth<=750 :
            label.config(font=('Countier', int(800/linewidth)))
        else:
            label.config(font=('Countier', 2))

        label.pack(side=RIGHT)
        f.close();
    #label.pack(side=RIGHT)
    blank2.grid(row=2, column = 0)
    frame_32.grid(row = 0, column = 1)
    frame_31.grid(row = 0,column = 0)
    #label = Label(frame_31, text="No Image Chosen")
    #label.pack(side=RIGHT)
    













 #    global blank2
 #    global label
 #    global frame3
 #    Grid.columnconfigure(root, 2, weight=1)
 #    Grid.rowconfigure(root, 2, weight=1)
 #    label.destroy()
 #    blank2.destroy()

 #    label = Label(frame2, image = photo )
 #    label.image = photo
 #    label.text = ""
	
 #    label.pack(side=LEFT)
	# #print(label)
 #    frame2.grid()
	#global label

 #    frame3 = Frame(root, bg= "White")
 #    frame3.grid(column = 1, row = 0)
 #    with open("temp.txt") as f:
 #        #line_width = f
 #        label = Label(frame3, text=f.read())
 #        label.config(font=('Countier', 5))
 #        label.pack(side=RIGHT)
 #        f.close();
	# #label.pack(side=RIGHT)

    root.after(delay, start)
    
	# image_file_path = tempdir
    # #image_width = sys.argv[2]
    # new_width = 
    # aspect_ratio = float(sys.argv[3])
    # print (new_width)

    # handle_image_conversion(image_file_path, new_width)

if __name__=='__main__':
    import sys
    
    Grid.rowconfigure(root, 3, weight = 1)
    root.title("Text_to_Unicode_Converter")
    root.geometry("1000x600+20+20")
    frame1 = Frame(root)
    frame1.grid(row = 0)
    frame2 = Frame(root)
    frame2.grid(row = 1)
    imageLabel = Label(frame1, text='Select your image').pack(side = LEFT)
    buttonUpload = Button(frame1, text='Browse', command = browse)
    buttonStart = Button(frame1, text='start', command = start)
    label = Label(frame1, text="Length:")
    global entry
    entry = Entry(frame1)
    buttonUpload.pack(side=LEFT)
    buttonStart.pack(side=LEFT)
    label.pack(side=LEFT)
    entry.pack(side=LEFT)
    entry.delete(0,END)
    entry.insert(0,750)

    buttonTw = Button(frame1, text='Twitch', command = twitch)
    buttonYt = Button(frame1, text='Youtube', command = youtube)
    buttonTw.pack(side=RIGHT)
    buttonYt.pack(side=RIGHT)

    #Labels
    global w1
    global w2
    global w3
    global w4

    label = Label(frame2, text="Contrast")
    label.pack(side=LEFT)
    w1 = Scale(frame2, from_=5, to=0, resolution=0.01)
    w1.set(1)
    w1.pack(side=LEFT)
     #Labels
    label = Label(frame2, text="Brightness")
    label.pack(side=LEFT)
    w2 = Scale(frame2, from_=5, to=0, resolution=0.01)
    w2.set(1)
    w2.pack(side=LEFT)
     #Labels
    label = Label(frame2, text="Color")
    label.pack(side=LEFT)
    w3 = Scale(frame2, from_=5, to=0, resolution=0.01)
    w3.set(1)
    w3.pack(side=LEFT)
     #Labels
    label = Label(frame2, text="Sharpness")
    label.pack(side=LEFT)
    w4 = Scale(frame2, from_=5, to=0, resolution=0.01)
    w4.set(1)
    w4.pack(side=LEFT)

    global blank2
    global frame_31
    global frame_32
    blank2 = Frame(root)
    Grid.columnconfigure(blank2, 2, weight = 1)
    Grid.rowconfigure(blank2, 1, weight = 1)
    blank2.grid(row=2)
    frame_31 = Frame(blank2)
    frame_31.grid(column = 0)

    frame_32 = Frame(blank2)
    frame_32.grid(column = 1)
    label = Label(frame_31, text="No Image Chosen")
    label.pack(side=LEFT)
    global label2
    label2 = Label(frame_32, text="No Image Conversion")
    label2.pack(side=RIGHT)
    #print (label)

    

    root.mainloop()