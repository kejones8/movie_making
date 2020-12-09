##Author: DLA & KJ, 03/2020

##This script makes a video from multiple files in the same directory
##I think I have tested cv2.imread (line 18) with both jpegs & pngs?

##**This requires installing opencv to import cv2. I had a bit of trouble getting it installed (several months ago), but I found lots of documentation online. 

import os
import cv2


outputName = 'movieName.avi' #name your movie
frameDir = '/home/dylananderson/projects/drifters/wamFrames/' #where are the images you want to make into a movie
files = os.listdir(frameDir) #create list of files
files.sort()
files_path = [os.path.join(frameDir,x) for x in os.listdir(frameDir)] #make list of files with their path
files_path.sort()
frame = cv2.imread(files_path[0])
height, width, layers = frame.shape #set the specifications for the movie frame
forcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(outputName, forcc, 8, (width, height)) #the numeric parameter in the middle controls the speed of the video, change this up or down to change play speed
for image in files_path:
    video.write(cv2.imread(image)) #actually write the video using every image in folder
cv2.destroyAllWindows()
video.release()
