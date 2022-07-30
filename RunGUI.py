# Importing necessary packages
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import font as tkFont
import os
import glob

# Defining CreateWidgets() function to
# create necessary tkinter widgets
def CreateWidgets():
	link_Label = Label(root, text ="  Select Image to be detected:   ",
					bg = "#E8D579",font = "Stencil", borderwidth=2, relief="solid")
	link_Label.grid(row = 1, column = 0,
					pady = 25, padx = 25)
	
	root.sourceText = Entry(root, width = 53,
							textvariable = sourceLocation, borderwidth=2, relief="solid")
	root.sourceText.grid(row = 2, column = 0,
						pady = 5, padx = 15,columnspan = 1,sticky=W)
	
	source_browseButton = Button(root, text ="Select Image",font=helv10, bg = "#E8D579", borderwidth=4,
                       relief=RAISED,
								command = SourceBrowse, width = 15)
	source_browseButton.grid(row = 2, column = 0,
							pady = 5, padx = 1,sticky=E)

	copyButton = Button(root, text ="Detect",font=helv15, bg = "#E8D579",
						command = CopyFile, width = 50, height = 1)
	copyButton.grid(row = 3, column = 0,
					pady = 10, padx = 15,sticky=EW)

	show_Button = Button(root, text ="Show result",font=helv15, bg = "#E8D579",
						command = Showimg, width = 50, height = 1)
	show_Button.grid(row = 5, column = 0,
					pady = 10, padx = 15,sticky=EW)

	



def Showimg():
	
    #Show the result image
	os.startfile("runs\detect\exp")


def SourceBrowse():

	root.sourceText.delete(0, END)
	# Opening the file-dialog directory prompting
	# the user to select files to copy using
	# filedialog.askopenfilenames() method. Setting
	# initialdir argument is optional Since multiple
	# files may be selected, converting the selection
	# to list using list()
	root.files_list = list(filedialog.askopenfilenames(initialdir ="dataset\images\train"))
	
	# Displaying the selected files in the root.sourceText
	# Entry using root.sourceText.insert()
	root.sourceText.insert('1', root.files_list)
	
def CopyFile():
	    
    #Cleaning previously annotated files
	dir = 'runs\detect'
	for files in os.listdir(dir):
		path = os.path.join(dir, files)
		try:
			shutil.rmtree(path)
		except OSError:
			os.remove(path)

	# Retrieving the source file selected by the
	# user in the SourceBrowse() and storing it in a
	# variable named files_list
	files_list = root.files_list

	#destinationLocation stored in a variable named 
	#destination_location
	destination_location = "data\images"

	# Looping through the files present in the list
	for f in files_list:
		
		# Copying the file to the destination using
		# the copy() of shutil module copy take the
		# source file and the destination folder as
		# the arguments
		shutil.copy(f, destination_location)

	messagebox.showinfo("IMAGE EXPORTED")
	os.system("python detect.py --source data/images/ --weights runs/train/exp/weights/best.pt")
	files = glob.glob('data\images\*')
	for f in files:
		os.remove(f)
    

# Creating object of tk class
root = tk.Tk()
helv15 = tkFont.Font(family='Helvetica', size=13, weight='bold')
helv10 = tkFont.Font(family='Helvetica', size=10, weight='bold')
# Setting the title and background color
# disabling the resizing property
root.geometry("600x520")
root.title(77*" "+"Detector")
root.config(background = "#344955")
	
# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()
	
# Calling the CreateWidgets() function
CreateWidgets()
	
# Defining infinite loop
root.mainloop()
