#Salvador Hernandez
#gets the user and downloads all images in a folder with the name of the folder
#as the name of the user
from urllib2 import urlopen
from urllib2 import urlparse
import urllib
from BeautifulSoup import BeautifulSoup
import os
import requests
import sys
from datetime import datetime
start_time = datetime.now()


inFile = sys.argv[1]
#runs = int(inFile)
#no longer needed
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

currentDirectory = os.getcwd()+"/"
#print currentDirectory

imgPath = currentDirectory+"data/images/"
myPath = currentDirectory+"data/users/"
#myPath = "/home/sal/Desktop/scrape/images/"
twitter = "https://twitter.com/"
url = ""


handle = inFile
url = twitter+handle+"/"
request = requests.get(url)


handle = handle.lower()
#open the url and reads the html
soup = BeautifulSoup(urlopen(url).read())
arr = []

#stores the image links into an array
#based on the img tag and src element
for element in soup.findAll('img'):
    source = element.get('src')
    if source != None:
    	arr.append(source)

#gets the unique links from the array
#uniqueLinks = remove_duplicates(arr)
uniqueLinks = list(set(arr))

count = 1
temp = ""

newFolder = imgPath+handle
if not os.path.exists(newFolder):
	os.makedirs(newFolder)

links = []
#downloads the images from the list
print "\n---------------\nDownloading from: "+handle+"\n---------------\n"
for i in uniqueLinks:
    links.append(i)
	#gets the last element from the link which is the name of the image itself
    temp = i.split("/")[-1:]
	#joins the path to the folder to the name of the image
	#fullfilename = os.path.join(myPath, temp[0])
    fullfilename = newFolder+"/"+temp[0]
	#downloads the image to the folder and names it the same as from where it was retrived from
    print("Downloading "+handle+": "+i)
    urllib.urlretrieve(i, fullfilename)
    count = count +1

#stores the image links onto a file
print("Writing to text file")
f = open(newFolder+"/"+"ImageLinks.txt", "w")
for i in links:
    f.write(i+"\n")
f.close()

# do your work here
end_time = datetime.now()
print('Done in: {}'.format(end_time - start_time))