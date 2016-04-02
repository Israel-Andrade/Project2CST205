#gets the average image...GIVEN THAT ALL IMAGES ARE THE SAME SIZE
import os, numpy, PIL
from PIL import Image
import scipy
import sys

#gets the text from the argument
inFile = sys.argv[1]

#Sets the paths
imageDirectory = os.getcwd()+"/data/images/"+inFile+"/"
averageImage = os.getcwd()+"/data/averageImages/"

#creates the folder if does not exist
if not os.path.exists(averageImage):
	os.makedirs(averageImage)

#gets all the files from the folder
allfiles=os.listdir(imageDirectory)
#gets all the images from the folder
imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG"]]

# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(imageDirectory+imlist[0]).size
N=len(allfiles)

# Create a numpy array of floats to store the average (assume RGB images)
arr=numpy.zeros((h,w,3),numpy.float)

#attempted to turn the RGBA images to RGB
'''
for im in imlist:
	image = Image.open(imageDirectory+im)
	print image.mode
	if(image.mode) != 'RGB':
		bg = Image.new("RGB", image.size, (255,255,255))
		bg.paste(image, (0,0), image)
		bg.save(imageDirectory+im, "PNG")
'''

rawr = []
largestW = 0
largestH = 0
# Build up average pixel intensities, casting each image as an array of floats
for im in imlist:
	w = 0
	h = 0

	#creates a numpy array from the image selected
	imarr=numpy.array(Image.open(imageDirectory+im),dtype=numpy.float)
	w,h=Image.open(imageDirectory+im).size

	#gets the largest width and height so that they can be used for the image that will be created
	if(w >= largestW):
		largestW = w
	if(h >= largestH):
		largestH = h
	#print("here")
   	#arr=arr+imarr/N
   	rawr.append(imarr)

N = len(imlist)

#creates the image with the alrgest width and height values
img = Image.new( 'RGB', (largestH, largestW), "black") # create a new black image
pixels = img.load() # create the pixel map

#will go through all the pixels getting the average and inserting into the pixel
for i in range(0,largestW):
   		for j in range(0,largestH):
   			totalR = []
   			totalG = []
   			totalB = []
   			length = N
   			check = 0
   			for k in range(0,N):
   				temp = rawr[k]
   				#checks for RGB enabled which have 3 values
   				if(len(temp.shape) < 3):
   					continue
   				#gets the values of width and height
				newH, newW, depth = temp.shape
				#checkc the size to see if the image has values in that pixel
   				if(i < newW and j < newH):
	   				R = temp[j][i][0]#gets Red
	   				G = temp[j][i][1]#gets Green
	   				B = temp[j][i][2]#gets Blue
	   				#appends the values to the commulative RGB lists
	   				totalR.append(R)
	   				totalG.append(G)
	   				totalB.append(B)
	   			else:
	   				#if the pixel is not present, decrease the length to obtain the right average
	   				length = length -1
	   				continue
	   		#compute the average		
   			newR = int(sum(totalR)/length)
   			newG = int(sum(totalG)/length)
   			newB = int(sum(totalB)/length)
   			#insert the new RGB values onto the image
   			pixels[i,j] = (newR, newG, newB)

img.save(averageImage+inFile+".jpeg", "JPEG")