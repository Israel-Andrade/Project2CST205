#Twitter Scrape GUI
#Salvador Hernandez
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
import os
import requests
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from urllib2 import urlparse
import urllib
import sys
from datetime import datetime

#generate path names
currentDirectory = os.getcwd()
myPath = currentDirectory+"/data/users/"
#myPath = "/home/sal/Desktop/scrape/images/"
twitter = "https://twitter.com/"
url = ""
imageDirectory = os.getcwd()+"/data/images/"
graphPath = currentDirectory+"/data/networks/"
averageImage = os.getcwd()+"/data/averageImages/"
#imageDirectory = "/home/sal/Desktop/data/images/"

#start the TK inter root
root = Tk()
check = 0

#this will scrape the twitter handle for users
def getUsers(tHandle):
	#starts timer for timing purposes
	start_time = datetime.now()
	handle = tHandle
	url = twitter+handle
	handle = handle.lower()
	
	#makes a requet baswd on the url with the handle to check if exists or not
	request = requests.get(url)

	#checks to see if the user exists
	if(request.status_code != 200):
	    print("Invalid twitter handle, Please try again")
	    return 
	else:
	    print("The handle exists!")
	print "\n---------------\nGetting users from: "+handle+"\n---------------\n"
	
	#open the url and reads the html
	soup = BeautifulSoup(urlopen(url).read())

	arr = []
	count = 0

	#gets the users and cleans them up and appends them to array arr
	for element in soup.findAll('a'):
	    dataScreenName = element.get('href')
	    if dataScreenName != None:
	        if dataScreenName.count('/') == 1 and dataScreenName.count('?') < 1:
	            temp = dataScreenName.split("/")[1]
	            if (temp.lower() != handle.lower() and temp !="" and temp!="tos" and temp!="privacy" and temp!="login" and temp!="about" and temp!="signup"):
	                #print temp
	                arr.append(temp.lower())
	                count = count +1

	#removes duplicates from the list of users
	usersFromHtml = list(set(arr))
	handlesFromUser= myPath

	#if the folder does not exist it creates it
	if not os.path.exists(handlesFromUser):
	    os.makedirs(handlesFromUser)
	f = open(handlesFromUser+handle+".txt", "w")

	#users are written to a text file
	for i in usersFromHtml:
	    f.write(i+"\n")
	    print "from "+handle+" : "+i
	f.close()
	
	#stops the timer
	end_time = datetime.now()
	#displays total time elapsed
	print('Done in: {}'.format(end_time - start_time))

#used to destroy images
def destroyImages():
	for i in xrange(len(pictureList)):
		pictureList[i].destroy()
		pictureList.remove(pictureList[i])
		destroyImages();

#used to check if the user exists
def checkUser(tHandle):
	handle = tHandle
	url = twitter+handle
	handle = handle.lower()
	#gets all the users from the html
	request = requests.get(url)
	if(request.status_code != 200):
	    print("Invalid twitter handle")
	    return 0
	else:
	    print("The handle exists!")
	    return 1

#grabs user input and initializes the process of scraping for users and creating the notebook tabs	    
def echo(*args):
	global check
	global tabs

	#gets user input
	temp = userInput.get()
	temp = temp.lower()
	output.set(temp)

	#checks if the twitter handle is valid
	valid = checkUser(temp)
	if(valid == 0):
		return
	
	#opens the user's profile on the web browser
	webbrowser.open("https://www.twitter.com/"+temp)

	#gets the images from the user
	os.system("python imgUser.py "+temp)
	endDir = imageDirectory+temp+"/"

	#gets all the images from the user
	allfiles=os.listdir(endDir)
	imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG"]]
	
	#sets the sizes for the notebooks
	tabWidth = 1600
	tabHeight = 1400

	if(check == 0):
		#sets up notebook widget on the mainFrame
		tabs = ttk.Notebook(mainFrame)
		tabs.grid(column=100, row=200, columnspan=3, rowspan=3)
		check+=1
	#redTab = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
	#greenTab = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
	#blueTab = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)

	#creates the tab that will contain the user images
	user = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
	#creates the tab that will contain the user's network map
	userNetwork = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
	#creates the tab that will contain the user's average image
	displayAvg = ttk.Frame(tabs, borderwidth=5, relief="sunken", width=tabWidth, height=tabHeight)
	
	#adds the tabs
	tabs.add(user, text = temp)
	tabs.add(userNetwork, text = temp+"Network")
	tabs.add(displayAvg, text = temp+"Avg")
	#tabs.add(user, text = temp+"Network")
	#tabs.add(redTab, text='Red')
	#tabs.add(greenTab, text ='Green')
	#tabs.add(blueTab, text ='Blue')

	#adds the image labels to a list
	test =[]
	for im in imlist:
		im  = Image.open(endDir+im)
		photo = ImageTk.PhotoImage(im)
		label = Label(user,image=photo)
		label.image = photo

		test.append(label)
	index = 0

	#inserts the images into the frame
	for row in range(0,5):
		for col in range(0,2):
			if(index >= len(test)):
				break
			test[index].grid(row = row, column = col)
			index+=1

	#gets the user's from the main user
	getUsers(temp)	
	#creates the networkmap
	os.system("python networkMap.py "+temp+".txt")

	#loads the image onto the user networkMap frame
	netWorkPath = graphPath+temp+"Network.png"
	image  = Image.open(netWorkPath)
	photo = ImageTk.PhotoImage(image)
	tLabel = Label(userNetwork,image=photo)
	tLabel.image = photo
	tLabel.grid(row=0, column=0)

	#gets the average image from the user and inserts it onto the frame
	os.system("python avgImages.py "+temp)
	avgImagePath = averageImage+temp+".jpeg"
	image  = Image.open(avgImagePath)
	photo = ImageTk.PhotoImage(image)
	aLabel = Label(displayAvg,image=photo)
	aLabel.image = photo
	aLabel.grid(row=0, column=0)

root.title("TWEET CREEP")
mainFrame = ttk.Frame(root)

#sets up the frame
frame = ttk.Frame(mainFrame, borderwidth=5, relief="sunken", width=100, height=200)




userInput = StringVar()
output = StringVar()

#make sure for each to insert into 'frame'
#sets up the Entry
userInput_entry = ttk.Entry(frame, width=7, textvariable=userInput)

#label will contain the variable output which will be what was entered on the field
outputLabel = ttk.Label(frame, textvariable=output)

#the button calls on the function 'echo' whcih redefined the variable 'output' to what was
#entered on the field
submitButton = ttk.Button(frame, text="submit", command=echo)
quitButton = ttk.Button(frame, text='Quit', command=quit)

#Labels
promptLabel = ttk.Label(frame, text="Twitter Handle:")
echoLabel = ttk.Label(frame, text="Recent: ")

#assign where the frames start in the root
mainFrame.grid(column=0, row=0)

#assign the startpoint and colspan and rowspan
frame.grid(column=0, row=0, columnspan=3, rowspan=3)

#namelbl.grid(column=3, row=0, columnspan=2)

#when the widgets are inserted, they are done so according to their frame!!!
promptLabel.grid(column=0, row=0, sticky= E)
userInput_entry.grid(column=1, row=0, sticky= W)

outputLabel.grid(column=1, row=1, sticky= W)
echoLabel.grid(column=0, row=1, sticky= E)

submitButton.grid(column=0,row=2)
quitButton.grid(column=1, row=2)

#binds the '<Return>' button to the function 'echo'

root.bind('<Return>', echo)

root.mainloop()