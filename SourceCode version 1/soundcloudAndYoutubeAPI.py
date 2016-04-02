#Name: Israel Andrade
#Description: Project 2
from Tkinter import *
from PIL import Image, ImageTk
from PIL import Image
from random import randint
import webbrowser
import vlc
import time
import soundcloud
import requests
import pygame
import pafy
import os

#our main widget/GUI
root = Tk()
instance = vlc.Instance()
isAudioOff = True
#Create a MediaPlayer with the default instance
player = instance.media_player_new()
#Path to the pictures
path = '/media/andrade/Storage/CST205/Project2/examples/'
#These text files will obtian our youtube url's
#We will open the or create a new text file
sadSongTextFile = open('sadSongs.txt', 'r')
happySongTextFile = open('happySongs.txt', 'r')
passionateSongTextFile = open('passionateSongs.txt', 'r')

#Make a list of the title of the songs
#This will allow you to pick from each song
redSongList = []
greenSongList = []
blueSongList = []
pictureList = []

"""
#Precondition: Three arguments will be passded in, the song URL from youtube, the folder name that
we want to place them in, and the color associated with that specific song will be stored it in the respective folder
#Postcondition: The function will download the specific songs from the urls 
#Summary: Function will download audio streams from youtube and songs will be placed in 
a folder specifing which song type they belong to
"""
def urlDownload(url, folderName, color):
		#Creating a new video instance
		video = pafy.new(url)
		print(video.title)
		#Veriable will hold the audiosteam 
		audiostreams = video.audiostreams
		#keeping track on the index to determine which audistream hold 
		#the mp4 or m4a extension 
		index = 0
		for a in audiostreams:
			print(a.bitrate, a.extension, a.get_filesize())
			if(a.extension == "mp4" or a.extension == "m4a"):
				print(index)
				folderPath = "/media/andrade/Storage/CST205/Project2/examples/" + folderName + "/"
				#create the directory if it does not exist
				if not os.path.exists(folderPath):
					os.mkdir(folderPath)
				#The name of song being passed in to our list
				x = video.title + ".mp4"
				#appending the song titles in their respective list
				if(color == 'red'):
					redSongList.append(x)
				elif(color == 'green'):
					greenSongList.append(x)
				elif(color == 'blue'):
					blueSongList.append(x)
				
				#The song path were we want to store our songs in
				songPath = folderPath + x

				#The below is commented because all songs have been downloaded
				#uncomment '#audiostreams[index].download(filepath = songPath)'' to download song stream

				"""
				#audiostreams[index].download(filepath = songPath)
				"""
				
				print("Downloaded")
				return;
			index+=1
"""
#Precondition: Three argument will be passed in: The text file with the URL's, the folder name, and the
color name associated with the songs passed in
#Postcondition: The songs will be placed in each a list, either redSongList, greenSongList, or blueSongList.
The list will hold the name of the songs
#Summary: This function will have three paraments which include the text file with
all the URL links to each specific song, the folder name to place these songs streams, and the color
associated with the song
"""	
def readInUrl(textFile, folderName, color):
	#This function will read in each line of text in our text file
	#If the line starts with an 'h', then we'll pass in that line to our other function
	#called urlDowload to download that audio stream from the url
	for line in textFile:
		if(line[0] == 'h'):
			urlDownload(line, folderName, color)

#We are going to call readInUrl funciton to store our songs in blueSongList
#The attribute to this folder will be sad/slow songs 
#Our blue songs will be stored in blueSongList and also in our folder 
#entitled sadSongs
folderName = "sadSongs" 
color = "blue"
readInUrl(sadSongTextFile, folderName, color)

#We are going to call each readInUrl function to store our songs in greenSongList
#The attribute to this folder will be happy/upbeat songs
#Our green songs will be stored in greenSongList and also in our folder
#entitled happySongs
folderName = "happySongs"
color = "green"
readInUrl(happySongTextFile, folderName, color)

#We are going to call each readInUrl function to store in our songs in redSongList
#The attribute to this folder will be passionate/
#Our red sonfs will be stored in redSongList and also in our folder
#entitled passionateSongs
folderName = "passionateSongs"
color = "red"
readInUrl(passionateSongTextFile, folderName, color)

"""
#Precondition: The redSongButton will be pressed
#Postcondition: The song will begin to play from our VLC instance
#Summary: This function will play songs from our redSongsList at random indexes
"""	
def redSongs():
	#Clean any preivous song info being displayed
	clearSongInfo()
	#Play a random song from our list from range 0 through 5
	randomIndex = randint(0,5)
	#Media to play in our player
	media = instance.media_new(path + "passionateSongs/" + redSongList[randomIndex])
	#Add the media to the player
	player.set_media(media)

	#stopAudio will appear after this function is called 
	#To ask if the user wishes to end the ceratin song playing
	stopAudio.grid(row = 2, column = 0)
	stopAudio.config(state = NORMAL)
	#The song will start playing
	player.play()
	#Display the song info at these coordinates
	songInfo.grid(row = 2, column = 1)
	songInfo.insert(END,"Now Playing " + redSongList[randomIndex])
"""
#Precondition: The greenSongButton will be pressed
#Postcondition: The song will begin to play from our VLC instance
#Summary: This function will play songs from our greenSongsList at random indexes
"""
def greenSongs():
	#Clean any preivous song info being displayed
	clearSongInfo()
	#Play a random song from our list from range 0 through 5
	randomIndex = randint(0,5)
	#Media to play in our player
	media = instance.media_new(path + "happySongs/" + greenSongList[randomIndex])
	#Add the media to the player
	player.set_media(media)

	#stopAudio will appear after this function is called 
	#To ask if the user wishes to end the ceratin song playing
	stopAudio.grid(row = 2, column = 0)
	stopAudio.config(state = NORMAL)
	#The song will start playing
	player.play()
	#Display the song info at these coordinates
	songInfo.grid(row = 2, column = 1)
	songInfo.insert(END,"Now Playing " + greenSongList[randomIndex])
"""
#Precondition: The blueSongButton will be pressed
#Postcondition: The song will begin to play from our VLC instance
#Summary: This function will play songs from our blueSongsList at random indexes
"""
def blueSongs():
	#Clean any preivous song info being displayed
	clearSongInfo()
	#Play a randon song from our list from range 0 through 5
	randomIndex = randint(0,5)
	#Media to play in our player
	media = instance.media_new(path + "sadSongs/" + blueSongList[randomIndex])
	#Add the media to the player
	player.set_media(media)
	#stopAudio will appear after this function is called 
	#To ask if the user wishes to end the ceratin song playingg
	stopAudio.grid(row = 2, column = 0)
	stopAudio.config(state = NORMAL)
	#The song will start playing
	player.play()
	#Display the song info at these coordinates
	songInfo.grid(row = 2, column = 1)
	songInfo.insert(END,"Now Playing " + blueSongList[randomIndex])
"""
#Precondition: The button stopAudio will be pressed
#Postcondition: The audio strem will stop playing
#Summary: This function will stop the audio stream from playing
"""	
def stopButton():
	player.stop()
	stopAudio.config(state = DISABLED)
	clearSongInfo()

"""
#Precondition: The button stopAudio will be pressed
#Postcondition: The function will delete the information in our songInfo Text field
#Summary: This function will clear the song information from our widget
"""	
def clearSongInfo():
	songInfo.delete('1.0', END)
"""
#Precondition: The soundcloud button will be pressed
#Postcondition: A new tab will be open in your webbrowser to display the soundcloud widget
#Summary: This function will display an HTML page with the soundcloud widget by opening up a webbrowser
"""	
def soundCloud():
	# create a client object with your app credentials
	client = soundcloud.Client(client_id='14678c3f68b575c72b22c1478c9e3d93')
	#make a list of urls to open up/
	#save into a list of file depending on saving memory and performance 
	track_url = 'https://soundcloud.com/octobersveryown/drake-back-to-back-freestyle'
	embed_info = client.get('/oembed', url=track_url)

	fileName = open('link.html', 'w')
	fileName.write(embed_info.html)
	path = '/media/andrade/Storage/CST205/Project2/examples/' + 'link.html'
	webbrowser.open_new_tab(path)	



#An empty list for all three RGB picture values is created to store
#each picture in their respective lsit
redPictures = []
greenPictures = []
bluePictures = []
#The RGB values for those pictures being passed in
red = 0
green = 0
blue = 0

"""
#Precondition: A picture name with its path will be passed in
#Postcondition: The picture will be stored in
#Summary: This function will obtain the average RGB values from each picture
and store them in a picture list based on their predominate color average
"""	
def averagePixel(pictureName):
	redValue = 0
	greenValue = 0
	blueValue = 0
	numPixels = 0
	im = Image.open(pictureName)
	pix = im.load()
	print im.size
	for x in xrange(im.size[0]):
		for y in xrange(im.size[1]):
			redValue += pix[x, y][0]
			greenValue += pix[x, y][1]
			blueValue += pix[x, y][2]
			numPixels += 1

	aveRed = redValue/numPixels
	aveGreen = greenValue/numPixels
	aveBlue = blueValue/numPixels
	print ("Average red is :"  , aveRed)
	print ("Average green is :" , aveGreen)
	print ("Average blue is : ", aveBlue)
	return aveRed, aveGreen, aveBlue

"""
#Precondition: The average RGB values and name of the picture will be passed in
#Postcondition: Each picture passed in will be placed in list based on the greates average RGB value
#Summary: This function will sort each picture to its a specific list 
depending on the greates color average in the picture
"""	
def sortColorPicture(red, green, blue, pictureName):
	if(red > green and red > blue):
		redPictures.append(pictureName)
	elif(green > red and green > blue):
		greenPictures.append(pictureName)
	elif(blue > red and blue > green):
		bluePictures.append(pictureName)

"""
#Precondition: A list of pictures must be passed in as the argument
#Postcondition: The images will be displayed in our GUI
#Summary: This function will display the image from each list in a row and column fromat using grids
"""	
def displayList(ListName):
	#The loop will go through each image in our list
	for im in ListName:
		#Make an instance of the image using PIL
		im = Image.open(im)
		#Creating an image instance using TKinter
		photo = ImageTk.PhotoImage(im)
		#Create a label with our image
		label = Label(image=photo)
		label.image = photo # keep a reference
		#append each label to our picture list
		pictureList.append(label)
	#Create a widget to in these coordinates
	#This widget will allow to hide the labels
	hidePictures.grid(row = 3, column = 0)
	#The structure function will be called to structure our display format for
	#each label
	structureFrameForPictures(pictureList)

"""
#Precondition: A list of picture will be passed in to display
#Postcondition: The list of picture labels will be displayed
#Summary: The function will structure each image based on the row and column
"""	
def structureFrameForPictures(nameOfPictureList):
	index = 0
	for row in range(5,9):
		for col in range(0,2):
			nameOfPictureList[index].grid(row = row, column = col)
			index+=1

"""
#Precondition: The hideButton will be pressed
#Postcondition: The pictures will be removed from our GUI
#Summary: This function will hide the pictures being displayed. If the user choices not to 
make the pictures displayed, he/she has the option to hide them from the user with the hideButton 
implemented in the code
"""	
def destroyListOfPictures():
		for i in xrange(len(pictureList)):
			pictureList[i].destroy()
			pictureList.remove(pictureList[i])
			destroyListOfPictures()


"""
#Precondition:
#Postcondition: The image will be placed in the list it belongs to 
ex. redPictures or bluePictures or greenPictures
#Summary: This function will place a picture in its repective list
"""	
def placePictureInList(pictureName):
	red, green, blue = averagePixel(pictureName)
	sortColorPicture(red, green, blue, pictureName)
	print ("red ", red)
	print ("green ", green)
	print ("blue ", blue)

placePictureInList('red.jpg')
placePictureInList('images.jpg')
placePictureInList('image.png')

def openRedPictures():
	displayList(redPictures)
def openGreenPictures():
	displayList(greenPictures)
def openBluePictures():
	displayList(bluePictures)

redButton = Button(root, text = 'Red Pictures', bg='red', fg='black', command = openRedPictures)
greenButton = Button(root, text = 'Green Pictures', bg = 'green', fg= 'black',command = openGreenPictures)
blueButton = Button(root, text = 'Blue Pictures', bg = 'blue', fg = 'black', command = openBluePictures)
hidePictures = Button(root, text = 'Hide Pictures', command = destroyListOfPictures)
redButton.grid(row = 0, column = 0)
greenButton.grid(row = 0, column = 1)
blueButton.grid(row = 0, column = 2)
soundcloudButton = Button(root, text = 'soundCloud', command = soundCloud)
soundcloudButton.grid(row = 1, column = 0)

redSongButton = Button(root, text = 'red song', bg = 'red', fg = 'black', command = redSongs)
redSongButton.grid(row = 1, column = 1)

greenSongButton = Button(root, text = 'green song', bg = 'green', fg = 'black', command = greenSongs)
greenSongButton.grid(row = 1, column = 2)

blueSongButton = Button(root, text = 'blue song', bg = 'blue', fg = 'black', command = blueSongs)
blueSongButton.grid(row = 1, column = 3)

stopAudio = Button(root, text = 'Stop Audio', command = stopButton)
songInfo = Text(root, height = 2, width = 30)
root.mainloop()