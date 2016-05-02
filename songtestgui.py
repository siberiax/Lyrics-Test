from Tkinter import *
import songtest
import sys

window = Tk()

historyList = []
historyString = []
historyText = []

def doHistory(a, s, r):
	x = len(historyList)
	if (x == 10):
		del historyString[0]
	else:
		text = StringVar()
		historyText.append(text)
		historyLabel = Label(frame4, textvariable=historyText[x], font=("Calibri", 12))
		historyList.append(historyLabel)
	if (r == 0):
		historyString.append(s + " by " + a + " was explicit")
	else:
		historyString.append(s + " by " + a + " was clean!")
	for x in range(len(historyList)):
		label = historyList[x]
		historyText[x].set(str(x+1) + ". " + historyString[x])
		label.grid(row=x)

def giveFeedback(result):
	string = ""
	if (result == 0):
		string = "song is explicit"
	elif (result == 1):
		string = "song is clean!"
	else:
		string = "there was an error :("

	resString.set(string)

def makeArtist():
	global artist
	global alabel
	alabel = StringVar()
	artist = Label(frame2, textvariable=alabel, font=("Calibri", 16))
	artist.grid(row=3)
	alabel.set("Artist:")

	global artistinput
	artistinput = StringVar()
	
	global artistr
	artistr = Entry(frame2, textvariable=artistinput, justify=CENTER, fg="gray")
	artistr.grid(row=4)
	artistr.bind('<Button-1>', cleartext1)
	artistr.bind('<Return>', getinput1)
	artistinput.set("Enter Artist")
	
	global enterArtist
	enterArtist = Button(frame2, text="Enter", command=getinput1)
	enterArtist.grid(row=5)

	global resString
	resString = StringVar()	
	
	global resLabel
	resLabel = Label(frame2, textvariable=resString, font=("calibri", 12))
	resLabel.grid(row=6)

def enterSongs(artist):
	alabel.set("Artist: " + artist)
	
	global songinput
	songinput = StringVar()
	
	global songr
	songr = Entry(frame2, textvariable=songinput, justify=CENTER, fg="gray")
	songr.grid(row=4)
	songr.bind('<Button-1>', cleartext2)
	songr.bind('<Return>', getinput2)
	songinput.set("Enter Song")
	
	global enterSong
	enterSong = Button(frame2, text="Enter", command=getinput2)
	enterSong.grid(row=5)

def cleartext1(event):
	artistr.delete(0, "end")
	artistr.config(fg="black")
	window.update()

def cleartext2(event):
	songr.delete(0, "end")
	songr.config(fg="black")
	window.update()

def getinput1(*event):
	global choice1
	choice1 = artistinput.get()
	if (choice1 != "Enter Artist"):
		enterSongs(choice1)

def getinput2(*event):
	choice2 = songinput.get()
	enterSong.focus()
	if (choice2 != "Enter Song"):
		songr.selection_clear()
		result = songtest.checkSong(choice1, choice2)
		giveFeedback(result)
		if (result != 2):
			doHistory(choice1, choice2, result)

def exitProgram():
	sys.exit()

def startOver():
	enterArtist.destroy()
	alabel.set("Artist:")
	resLabel.destroy()
	makeArtist()

frame3 = Frame(window)
frame3.pack()
frame1 = Frame(frame3)
frame1.grid(row=2)
frame2 = Frame(frame3)
frame2.grid(row=2, column=1)
frame4 = Frame(frame3)
frame4.grid(row=4, columnspan=2)

title = Label(frame3, text="Are these songs clean?", font=("Calibri", 20)).grid(row=0)
sig = Label(frame3, text="by Alex McHugh", font=("Calibri", 12)).grid(row=1)

img1 = PhotoImage(file="headphone.gif")
img2 = PhotoImage(file="guitar.gif")
img3 = PhotoImage(file="microphone.gif")
img4 = PhotoImage(file="musicnote.gif")
image1 = Label(frame1, image=img1).grid(row=2, column=0)
image2 = Label(frame1, image=img2).grid(row=2, column=1)
image3 = Label(frame1, image=img3).grid(row=3, column=0)
image4 = Label(frame1, image=img4).grid(row=3, column=1)

startover = Button(frame3, text="Change Artist", command=startOver).grid(row=0, column=1)
exit = Button(frame3, text="Exit", command=exitProgram)
exit.grid(row=1,column=1)

history = Label(frame3, text="History", font=("Calibri",20)).grid(row=3, columnspan=2)

makeArtist()

window.wm_title("Lyrics Test")
window.geometry("+%d+%d" % (465, 134))

window.resizable(width=FALSE, height=FALSE)

window.mainloop()